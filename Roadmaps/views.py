from django.shortcuts import render
from rest_framework import generics, status
from .serializers import *
from Users.models import MyUser
from rest_framework.response import Response
from django.http import JsonResponse
from Commonclasses.models import Lecture as CommonLecture
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
# Create your views here.



# 새로 짠거 # 
##########################################

class RoadmapFullView(generics.ListAPIView):
    queryset = Roadmap.objects.all()
    serializer_class = RoadMapSerializer

    
    
    def get(self, request, *args, **kwargs):
        logged_user = request.user
        user_id = logged_user.student_number
        
        user = MyUser.objects.get(student_number=user_id)
        roadmaps = Roadmap.objects.filter(student=user)
        print(roadmaps)
        roadmap_data = {'roadmaps': []}

        for roadmap in roadmaps:
            roadmap_info = RoadMapSerializer(roadmap).data
            roadmap_details = RoadmapDetail.objects.filter(roadmap=roadmap)
            roadmap_info['roadmap_detail'] = []  

            for detail in roadmap_details:
                detail_data = RoadMapDetailSerializer(detail).data
                semester = detail_data['semester']
                detail_lectures = RoadmapDetailLecture.objects.filter(roadmap_detail=detail)
                lectures_data = RoadMapDetailLectureSerializer(detail_lectures, many=True).data
                detail_data['roadmapdetaillecture'] = {semester: lectures_data}  
                roadmap_info['roadmap_detail'].append(detail_data['roadmapdetaillecture']) 

            roadmap_data['roadmaps'].append(roadmap_info)

        return JsonResponse(roadmap_data['roadmaps'], safe=False)


############################################################################################################################################################
# 1. 전공에 따라서 어떤 track이 있는지와 본전공을 제외한 전공 데이터들을 보내줘야됨. 근데 본전공 제외 전공데이터들까지 내가 해줘야되는진 잘 모르겠음.
class TrackByMajor(APIView):
    serializer_class = UserMajorTrackSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user_a = request.user
        serialized_data = self.serializer_class(user_a).data
        return Response(serialized_data)
        

# 1.5. 공통고르는건 똑같으니까 공통 데이터부터 보내주자.
class CommonDutyLectureListView(generics.ListAPIView):
    serializer_class = CommonLectureListSerializer

    def get_category_point(self, category_name):
        # category_name을 기반으로 포인트를 동적으로 설정
        student_year = self.request.user.student_year
        if student_year == 21 and category_name == '소프트웨어':
            return 0
        elif category_name == '서강인성':
            return 1
        elif category_name == '글쓰기':
            return 3
        elif category_name == '글로벌 언어1':
            return 3
        elif category_name == '전공 진로 탐색':
            return 1
        elif category_name == '소프트웨어':
            return 3
        # 나머지 경우에 대한 처리

    def get_queryset(self):
        student_year = self.request.user.student_year
        category_field_name = f"category{student_year}"
        category_names = ['서강인성', '글쓰기', '글로벌 언어1', '전공 진로 탐색', '소프트웨어']
        queryset = []

        for category_name in category_names:
            category_point = self.get_category_point(category_name)
            category = Category.objects.get(detail=category_name)

            if (self.request.user.major.title == '경영' or self.request.user.major.title == '경제') and category_name == '글쓰기':
                lectures = CommonLecture.objects.filter(
                    **{category_field_name: category, 'title': '인문사회 글쓰기'}
                )
            elif self.request.user.major.title == '컴퓨터공학' and category_name == '글쓰기':
                lectures = CommonLecture.objects.filter(
                    **{category_field_name: category, 'title': '자연계 글쓰기'}
                )
            elif self.request.user.major.title == '경영' and category_name == '전공 진로 탐색':
                lectures = CommonLecture.objects.filter(
                    **{category_field_name: category, 'title': '알바트로스 세미나(경영)'}
                )
            elif (self.request.user.major.title == '경제' or self.request.user.major.title == '컴퓨터공학') and category_name == '전공 진로 탐색':
                lectures = CommonLecture.objects.filter(
                    **{category_field_name: category, 'title': '알바트로스 세미나'}
                )
            else:
                lectures = CommonLecture.objects.filter(**{category_field_name: category})

            queryset.append({
                category_name: category_point,
                'lectures': self.serializer_class(lectures, many=True).data
            })

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)

class CommonChoiceLectureListView(generics.ListAPIView):
    serializer_class = CommonLectureListSerializer

    def get_category_point(self, category_name):
        # category_name을 기반으로 포인트를 동적으로 설정
        if category_name == '인간과 신앙':
            return 3
        elif category_name == '인간과 사상':
            return 3
        elif category_name == '인간과 사회':
            return 3
        elif category_name == '인간과 과학':
            return 3
        # 나머지 경우에 대한    처리

    def get_queryset(self):
        student_year = self.request.user.student_year
        category_field_name = f"category{student_year}"
        category_names = ['인간과 신앙', '인간과 사상', '인간과 사회', '인간과 과학']
        queryset = []

        for category_name in category_names:
            category_point = self.get_category_point(category_name)
            category = Category.objects.get(detail=category_name)
            
            if self.request.user.major.title == '컴퓨터공학' and category_name == '인간과 과학':
        # '경영' 전공인 경우 '글쓰기' 카테고리에 대한 추가 필터링
                lectures = CommonLecture.objects.filter(
                **{category_field_name: category, 'title': '미적분학1'}  # 필터링 조건 추가
                )
            else:
                lectures = CommonLecture.objects.filter(**{category_field_name: category})
            
            queryset.append({
                category_name: category_point,
                'lectures': self.serializer_class(lectures, many=True).data
            })

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
# 2. 프론트로부터 고른 track과 다전공일때의 부전공을 받았을때 부전공이 null인지 1개인지 2개인지를 확인.

############################################################################################################################################################
class DoneLectures(generics.ListAPIView):
    serializer_class = alllectures
    def get_queryset(self):
        user_request = request.user
        completed_lecture = UserCommonLecture.objects.filter(user=user_request).values_list('commonlecture_id', flat=True)
        uncompleted_lectures = CommonLecture.objects.exclude(id__in=completed_lecture)
        search_keyword = self.request.query_params.get('title', None)
        if search_keyword is not None:
            uncompleted_lectures = uncompleted_lectures.filter(title__icontains=search_keyword)
        return uncompleted_lectures
# 3. 이수한것들 등록하는 url
########################################################################################################################################################################3

# 4. 컴공
class CSEGichoLectureListView(generics.ListAPIView):
    serializer_class = CSELectureDetailSerializer

    # 프론트로부터 user가 고른 track의 pk를 받아서, related_name을 통해서 track_CSEtrack을 통해서 각 category_point를 불러옴.
    def get_category_point(self, category_name):
        track_pk = self.kwargs['track_pk']
        track = CSETrack.objects.get(pk=track_pk)
        major_track = track.track_CSEtrack.first()  # 첫 번째 MajorTrack을 선택합니다.
        if major_track is not None:
            return major_track.gicho_point
        else:
            return None  # 또는 적절한 디폴트값을 반환할 수 있습니다.

    def get_queryset(self, request):
        student_year = self.request.user.student_year
        category_field_name = f"category{student_year}"
        category_name = '전공입문교과'
        category_details = ['']
        queryset = []
        user_request = request.user
        completed_lecture = UserCSELecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        categories = Category.objects.filter(title=category_name)  # Use filter instead of get
        for category in categories:
            
            # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
            lectures = CSELecture.objects.filter(**{category_field_name: category}).exclude(id__in=completed_lecture)
            queryset.append({
                category.detail: category_point,
                'lectures': self.serializer_class(lectures, many=True).data
            })

        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)

class CSEDutyLectureListView(generics.ListAPIView):
    serializer_class = CSELectureDetailSerializer

    # 프론트로부터 user가 고른 track의 pk를 받아서, related_name을 통해서 track_CSEtrack을 통해서 각 category_point를 불러옴.
    def get_category_point(self, category_name):
        track_pk = self.kwargs['track_pk']
        track = CSETrack.objects.get(pk=track_pk)
        major_track = track.track_CSEtrack.first()  # 첫 번째 MajorTrack을 선택합니다.
        if major_track is not None:
            return major_track.duty_point
        else:
            return None  # 또는 적절한 디폴트값을 반환할 수 있습니다.

    def get_queryset(self):
        student_year = self.request.user.student_year
        category_field_name = f"category{student_year}"
        print(category_field_name)
        category_name = '전공필수교과'
        category_details = ['']
        queryset = []
        user_request = request.user
        completed_lecture = UserCSELecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        categories = Category.objects.filter(title=category_name)  # Use filter instead of get
        for category in categories:
            
            # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
            lectures = CSELecture.objects.filter(**{category_field_name: category}).exclude(id__in=completed_lecture)
            queryset.append({
                category.detail: category_point,
                'lectures': self.serializer_class(lectures, many=True).data
            })

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class CSEChoiceLectureListView(generics.ListAPIView):
    serializer_class = CSELectureDetailSerializer

    # 프론트로부터 user가 고른 track의 pk를 받아서, related_name을 통해서 track_CSEtrack을 통해서 각 category_point를 불러옴.
    def get_category_point(self, category_name):
        track_pk = self.kwargs['track_pk']
        track = CSETrack.objects.get(pk=track_pk)
        major_track = track.track_CSEtrack.first()  # 첫 번째 MajorTrack을 선택합니다.
        if major_track is not None:
            return major_track.choice_point
        else:
            return None  # 또는 적절한 디폴트값을 반환할 수 있습니다.

    def get_queryset(self):
        student_year = self.request.user.student_year
        category_field_name = f"category{student_year}"
        print(category_field_name)
        category_name = '전공선택교과'
        category_details = ['']
        queryset = []
        user_request = request.user
        completed_lecture = UserCSELecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        categories = Category.objects.filter(title=category_name)  # Use filter instead of get
        for category in categories:
            
            # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
            lectures = CSELecture.objects.filter(**{category_field_name: category}).exclude(id__in=completed_lecture)
            queryset.append({
                category.detail: category_point,
                'lectures': self.serializer_class(lectures, many=True).data
            })

        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
##########################################################################################################################3333
# 경영
class MGTGichoLectureListView(generics.ListAPIView):

    serializer_class = MGTLectureDetailSerializer

    # 프론트로부터 user가 고른 track의 pk를 받아서, related_name을 통해서 track_CSEtrack을 통해서 각 category_point를 불러옴.
    def get_category_point(self, category_name):
        track_pk = self.kwargs['track_pk']
        track = MGTTrack.objects.get(pk=track_pk)
        major_track = track.track_MGTtrack.first()  # 첫 번째 MajorTrack을 선택합니다.
        if major_track is not None:
            return major_track.gicho_point
        else:
            return None  # 또는 적절한 디폴트값을 반환할 수 있습니다.

    def get_queryset(self):
        student_year = self.request.user.student_year
        category_field_name = f"category{student_year}"
        print(category_field_name)
        category_name = '전공입문교과'
        category_details = ['']
        queryset = []
        user_request = request.user
        completed_lecture = UserMGTLecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        categories = Category.objects.filter(title=category_name)  # Use filter instead of get
        for category in categories:
            
            # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
            lectures = MGTLecture.objects.filter(**{category_field_name: category}).exclude(id__in=completed_lecture)
            queryset.append({
                category.detail: category_point,
                'lectures': self.serializer_class(lectures, many=True).data
            })

        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)

class MGTDutyLectureListView(generics.ListAPIView):
    serializer_class = MGTLectureDetailSerializer

    # 프론트로부터 user가 고른 track의 pk를 받아서, related_name을 통해서 track_CSEtrack을 통해서 각 category_point를 불러옴.
    def get_category_point(self, category_name):
        track_pk = self.kwargs['track_pk']
        track = MGTTrack.objects.get(pk=track_pk)
        major_track = track.track_MGTtrack.first()  # 첫 번째 MajorTrack을 선택합니다.
        if major_track is not None:
            return major_track.duty_point
        else:
            return None  # 또는 적절한 디폴트값을 반환할 수 있습니다.

    def get_queryset(self):
        student_year = self.request.user.student_year
        category_field_name = f"category{student_year}"
        print(category_field_name)
        category_name = '전공필수교과'
        category_details = ['']
        queryset = []
        user_request = request.user
        completed_lecture = UserMGTLecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        categories = Category.objects.filter(title=category_name)  # Use filter instead of get
        for category in categories:
            major_techs = MajorTech.objects.all()
            for major_tech in major_techs:
            # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
                lectures = MGTLecture.objects.filter(**{category_field_name: category}, tech=major_tech).exclude(id__in=completed_lecture)
                if lectures.exists():  # Check if there are any lectures for this combination
                    queryset.append({
                        'major_tech_title': major_tech.title,
                        'lectures': self.serializer_class(lectures, many=True).data
                    })

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class MGTChoiceLectureListView(generics.ListAPIView):
    serializer_class = MGTLectureDetailSerializer

    # 프론트로부터 user가 고른 track의 pk를 받아서, related_name을 통해서 track_CSEtrack을 통해서 각 category_point를 불러옴.
    def get_category_point(self, category_name):
        track_pk = self.kwargs['track_pk']
        track = MGTTrack.objects.get(pk=track_pk)
        major_track = track.track_MGTtrack.first()  # 첫 번째 MajorTrack을 선택합니다.
        if major_track is not None:
            return major_track.choice_point
        else:
            return None  # 또는 적절한 디폴트값을 반환할 수 있습니다.

    def get_queryset(self):
        student_year = self.request.user.student_year
        category_field_name = f"category{student_year}"
        print(category_field_name)
        category_name = '전공선택교과'
        category_details = ['']
        queryset = []
        user_request = request.user
        completed_lecture = UserMGTLecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        categories = Category.objects.filter(title=category_name)  # Use filter instead of get
        for category in categories:
            major_techs = MajorTech.objects.all()
            for major_tech in major_techs:
            # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
                lectures = MGTLecture.objects.filter(**{category_field_name: category}, tech=major_tech).exclude(id__in=completed_lecture)
                if lectures.exists():  # Check if there are any lectures for this combination
                    queryset.append({
                        'major_tech_title': major_tech.title,
                        'lectures': self.serializer_class(lectures, many=True).data
                    })

        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
#####################################################################################################################################
#6.경제
class ECOGichoLectureListView(generics.ListAPIView):

    serializer_class = ECOLectureDetailSerializer

    # 프론트로부터 user가 고른 track의 pk를 받아서, related_name을 통해서 track_CSEtrack을 통해서 각 category_point를 불러옴.
    def get_category_point(self, category_name):
        track_pk = self.kwargs['track_pk']
        track = ECOTrack.objects.get(pk=track_pk)
        major_track = track.track_ECOtrack.first()  # 첫 번째 MajorTrack을 선택합니다.
        if major_track is not None:
            return major_track.gicho_point
        else:
            return None  # 또는 적절한 디폴트값을 반환할 수 있습니다.

    def get_queryset(self):
        student_year = self.request.user.student_year
        category_field_name = f"category{student_year}"
        print(category_field_name)
        category_name = '전공입문교과'
        category_details = ['']
        queryset = []
        user_request = request.user
        completed_lecture = UserECOLecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        categories = Category.objects.filter(title=category_name)  # Use filter instead of get
        for category in categories:
            
            # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
            lectures = MGTLecture.objects.filter(**{category_field_name: category}).exclude(id__in=completed_lecture)
            queryset.append({
                category.detail: category_point,
                'lectures': self.serializer_class(lectures, many=True).data
            })

        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)

class ECODutyLectureListView(generics.ListAPIView):
    serializer_class = ECOLectureDetailSerializer

    # 프론트로부터 user가 고른 track의 pk를 받아서, related_name을 통해서 track_CSEtrack을 통해서 각 category_point를 불러옴.
    def get_category_point(self, category_name):
        track_pk = self.kwargs['track_pk']
        track = ECOTrack.objects.get(pk=track_pk)
        major_track = track.track_ECOtrack.first()  # 첫 번째 MajorTrack을 선택합니다.
        if major_track is not None:
            return major_track.duty_point
        else:
            return None  # 또는 적절한 디폴트값을 반환할 수 있습니다.

    def get_queryset(self):
        student_year = self.request.user.student_year
        category_field_name = f"category{student_year}"
        print(category_field_name)
        category_name = '전공필수교과'
        category_details = ['']
        queryset = []
        user_request = request.user
        completed_lecture = UserECOLecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        categories = Category.objects.filter(title=category_name)  # Use filter instead of get
        for category in categories:
            major_techs = MajorTech.objects.all()
            for major_tech in major_techs:
            # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
                lectures = ECOLecture.objects.filter(**{category_field_name: category}, tech=major_tech).exclude(id__in=completed_lecture)
                if lectures.exists():  # Check if there are any lectures for this combination
                    queryset.append({
                        'major_tech_title': major_tech.title,
                        'lectures': self.serializer_class(lectures, many=True).data
                    })

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class ECOChoiceLectureListView(generics.ListAPIView):
    serializer_class = ECOLectureDetailSerializer

    # 프론트로부터 user가 고른 track의 pk를 받아서, related_name을 통해서 track_CSEtrack을 통해서 각 category_point를 불러옴.
    def get_category_point(self, category_name):
        track_pk = self.kwargs['track_pk']
        track = ECOTrack.objects.get(pk=track_pk)
        major_track = track.track_ECOtrack.first()  # 첫 번째 MajorTrack을 선택합니다.
        if major_track is not None:
            return major_track.choice_point
        else:
            return None  # 또는 적절한 디폴트값을 반환할 수 있습니다.

    def get_queryset(self):
        student_year = self.request.user.student_year
        category_field_name = f"category{student_year}"
        print(category_field_name)
        category_name = '전공선택교과'
        category_details = ['']
        queryset = []
        user_request = request.user
        completed_lecture = UserECOLecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        categories = Category.objects.filter(title=category_name)  # Use filter instead of get
        for category in categories:
            major_techs = MajorTech.objects.all()
            for major_tech in major_techs:
            # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
                lectures = ECOLecture.objects.filter(**{category_field_name: category}, tech=major_tech).exclude(id__in=completed_lecture)
                if lectures.exists():  # Check if there are any lectures for this combination
                    queryset.append({
                        'major_tech_title': major_tech.title,
                        'lectures': self.serializer_class(lectures, many=True).data
                    })

        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
####################################################################################################################################################333
# 로드맵 디테일 자동으로 완성 작성
class RoadmapDetailCreateView(APIView):
    def post(self, request, format=None):
        serializer = RoadmapDetailCreateSerializer(data=request.data)
        if serializer.is_valid():
            roadmap_id = serializer.save()  # Save returns roadmap_id
            return Response(f"RoadmapDetails created successfully for Roadmap {roadmap_id}", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)