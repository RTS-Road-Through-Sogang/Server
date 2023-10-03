from django.shortcuts import render
from rest_framework import generics, status
from .serializers import *
from Users.models import MyUser
from rest_framework.response import Response
from django.http import JsonResponse
from Commonclasses.models import Lecture as CommonLecture
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.db.models import Q

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
# 검색결과를 보여주는 것
class CompletedSerachListAPIView(generics.ListAPIView):
    queryset = CommonLecture.objects.all()
    serializer_class = alllectures

    def list(self, request, *args, **kwargs):
        keyword = request.query_params.get('keyword', None)
        print(keyword)
        queryset = self.get_queryset()
        try:
            conditions = Q()
            if keyword:
                conditions |= Q(title__icontains=keyword)
            queryset = queryset.filter(conditions)
        except Exception as e:
            return Response({'message': 'Filtering Error Occurred, Sorry'}, status=status.HTTP_404_NOT_FOUND)
        serializer = alllectures(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
            roadmap_id = serializer.save() 
            return Response(f"RoadmapDetails created successfully for Roadmap {roadmap_id}", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#########################################################################################
# 로드맵에 과목 넣어주기
class RoadmapDetailLectureCreateView(APIView):
    def post(self, request, format=None):
        # 1. Serializer 인스턴스 생성
        serializer = RoadmapDetailLectureCreateSerializer(data=request.data)

        # 2. 데이터 유효성 검사
        if serializer.is_valid():
            roadmap_detail_id = serializer.validated_data.get('roadmap_detail_id')
            lecture_type = serializer.validated_data.get('lecture_type')
            lecture_id = serializer.validated_data.get('lecture_id')
            
            try:
                if lecture_type == 'commonlecture':
                    roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                    commonlecture = CommonLecture.objects.get(pk=lecture_id)
                    obj = RoadmapDetailLecture.objects.create(
                        roadmap_detail=roadmap_detail,
                        commonlecture=commonlecture
                    )
                elif lecture_type == 'cselecture':
                    roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                    cselecture = CSELecture.objects.get(pk=lecture_id)
                    obj = RoadmapDetailLecture.objects.create(
                        roadmap_detail=roadmap_detail,
                        cselecture=cselecture
                    )
                elif lecture_type == 'ecolecture':
                    roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                    ecolecture = ECOLecture.objects.get(pk=lecture_id)
                    obj = RoadmapDetailLecture.objects.create(
                        roadmap_detail=roadmap_detail,
                        ecolecture=ecolecture
                    )
                elif lecture_type == 'mgtlecture':
                    roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                    commonlecture = CommonLecture.objects.get(pk=lecture_id)
                    obj = RoadmapDetailLecture.objects.create(
                        roadmap_detail=roadmap_detail,
                        commonlecture=commonlecture
                    )
                else:
                    raise serializers.ValidationError("Invalid lecture type")

            except RoadmapDetail.DoesNotExist as e:
                return Response({"error": f"RoadmapDetail with id {roadmap_detail_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)
            except CommonLecture.DoesNotExist as e:
                return Response({"error": f"CommonLecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)
            except CSELecture.DoesNotExist as e:
                return Response({"error": f"CSELecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)
            except ECOLecture.DoesNotExist as e:
                return Response({"error": f"ECOLecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)
            except MGTLecture.DoesNotExist as e:
                return Response({"error": f"MGTLecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # 원하는 작업을 수행한 후 응답을 반환하거나, 다른 처리를 수행할 수 있습니다.
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # 유효성 검사에 실패한 경우 에러 응답 반환
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##################################################################################################
# 이수한 놈들 추가할 수 있는 코드
class CompletedLectureCreateView(APIView):
    def post(self, request, format=None):
        serializer = CompletedLectureCreateSerializer(data=request.data)
        user_id = self.request.user
        
        if serializer.is_valid():
            lecture_type = serializer.validated_data.get('lecture_type')
            lecture_id = serializer.validated_data.get('lecture_id')
            
            try:
                if lecture_type == 'commonlecture':
                    commonlecture = CommonLecture.objects.get(pk=lecture_id)
                    obj = UserCommonLecture.objects.create(
                        user=user_id,
                        commonlecture=commonlecture
                    )
                elif lecture_type == 'cselecture':
                    cselecture = CSELecture.objects.get(pk=lecture_id)
                    obj = UserCSELecture.objects.create(
                        user=user_id,
                        cselecture=cselecture
                    )
                elif lecture_type == 'ecolecture':
                    ecolecture = ECOLecture.objects.get(pk=lecture_id)
                    obj = UserECOLecture.objects.create(
                        user=user_id,
                        ecolecture=ecolecture
                    )
                elif lecture_type == 'mgtlecture':
                    commonlecture = CommonLecture.objects.get(pk=lecture_id)
                    obj = UserMGTLecture.objects.create(
                        user=user_id,
                        commonlecture=commonlecture
                    )
                else:
                    raise serializers.ValidationError("Invalid lecture type")

            except CommonLecture.DoesNotExist as e:
                return Response({"error": f"CommonLecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)
            except CSELecture.DoesNotExist as e:
                return Response({"error": f"CSELecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)
            except ECOLecture.DoesNotExist as e:
                return Response({"error": f"ECOLecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)
            except MGTLecture.DoesNotExist as e:
                return Response({"error": f"MGTLecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "Object created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#################################################################################################