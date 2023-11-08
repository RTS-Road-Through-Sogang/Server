from django.shortcuts import render
from rest_framework import generics, status
from .serializers import *
from Users.models import MyUser
from rest_framework.response import Response
from django.http import JsonResponse

from Commonclasses.models import Lecture as CommonLecture
from CSEclasses.models import Track as CSETrack
from MGTclasses.models import Track as MGTTrack
from ECOclasses.models import Track as ECOTrack

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
##########################################################################################################################################################
class RoadmapDefaultView(generics.ListAPIView):
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
                detail_lectures = RoadmapDetailLecture.objects.filter(roadmap_detail=detail,completed=True)
                lectures_data = RoadMapDetailLectureSerializer(detail_lectures, many=True).data
                detail_data['roadmapdetaillecture'] = {semester: lectures_data} 
                if detail_lectures.commonlecture:
                    former = detail_lectures.commonlecture.former
                    eta = detail_lectures.commonlecture.eta
                    semester_one = detail_lectures.commonlecture.semester_one
                    semester_two = detail_lectures.commonlecture.semester_two
                    
                    
                elif detail_lectures.cselecture:
                    former = detail_lectures.cselecture.former
                    eta = detail_lectures.cselecture.eta
                    semester_one = detail_lectures.cselecture.semester_one
                    semester_two = detail_lectures.cselecture.semester_two
                
                elif detail_lectures.mgtlecture:
                    former = detail_lectures.mgtlecture.former
                    eta = detail_lectures.mgtlecture.eta
                    semester_one = detail_lectures.mgtlecture.semester_one
                    semester_two = detail_lectures.mgtlecture.semester_two
                    
                else:
                    
                    former = detail_lectures.ecolecture.former
                    eta = detail_lectures.ecolecture.eta
                    semester_one = detail_lectures.ecolecture.semester_one
                    semester_two = detail_lectures.ecolecture.semester_two
                    
                
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
        
class PointsListView(generics.ListAPIView):
    mgtserializer_class = MGTMajorTrackSerializer
    ecoserializer_class = ECOMajorTrackSerializer
    cseserializer_class = CSEMajorTrackSerializer
    def get_queryset(self):
        queryset = []
        #student_year, track, major, submajor를 받아와서 채워줘야됨
        student_year = self.request.user.student_year
        track_pk = self.kwargs['track_pk']
        major = self.request.user.major.title
        if major == '경영':
            points = MGTMajorTrack.objects.filter(track=track_pk).first()
            queryset.append({
                'points': self.mgtserializer_class(points).data
            })
        elif major == '경제':
            points = ECOMajorTrack.objects.filter(track=track_pk).first()
            queryset.append({
                'points': self.ecoserializer_class(points).data
            })
        elif major == '컴퓨터공학':
            points = CSEMajorTrack.objects.filter(track=track_pk).first()
            queryset.append({
                'points': self.cseserializer_class(points).data
            })
        #만약 다전공이라면:
        submajor = self.request.data.get('submajor', None)
        if major == '경영':
            if track_pk == 1 or track_pk == 2 or track_pk == 3:
                if submajor == '경제':
                    subtrack = ECOTrack.objects.filter(title="다전공 타전공", student_year=student_year).first()
                    subpoints = ECOMajorTrack.objects.filter(track=subtrack).first()
                    queryset.append({
                        'subpoints': self.ecoserializer_class(subpoints).data
                    })
                elif submajor == '컴퓨터공학과':
                    subtrack = CSETrack.objects.filter(title="다전공 타전공", student_year=student_year).first()
                    subpoints = CSEMajorTrack.objects.filter(track=subtrack).first()
                    queryset.append({
                        'subpoints': self.cseserializer_class(subpoints).data
                    })
        elif major == '경제':
            if track_pk == 1 or track_pk == 2 or track_pk == 3:
                if submajor == '경영':
                    subtrack = MGTTrack.objects.filter(title='다전공 타전공', student_year=student_year-20).first()
                    print(subtrack)
                    subpoints = MGTMajorTrack.objects.filter(track=subtrack).first()
                    queryset.append({
                        'subpoints': self.mgtserializer_class(subpoints).data
                    })
                elif submajor == '컴퓨터공학과':
                    subtrack = CSETrack.objects.filter(title="다전공 타전공", student_year=student_year).first()
                    subpoints = CSEMajorTrack.objects.filter(track=subtrack).first()
                    queryset.append({
                        'subpoints': self.cseserializer_class(subpoints).data
                    })
        elif major == '컴퓨터공학':
            if track_pk == 3 or track_pk == 8 or track_pk == 13:
                if submajor == '경제':
                    subtrack = ECOTrack.objects.filter(title="다전공 타전공", student_year=student_year).first()
                    subpoints = ECOMajorTrack.objects.filter(track=subtrack).first()
                    queryset.append({
                        'subpoints': self.ecoserializer_class(subpoints).data
                    })
                elif submajor == '경영':
                    subtrack = MGTTrack.objects.filter(title="다전공 타전공", student_year=student_year).first()
                    subpoints = MGTMajorTrack.objects.filter(track=subtrack).first()
                    queryset.append({
                        'subpoints': self.mgtserializer_class(subpoints).data
                    })

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
    
# 1.5. 공통고르는건 똑같으니까 공통 데이터부터 보내주자.
class CommonDutyLectureListView(generics.ListAPIView):
    serializer_class = CommonLectureListSerializer
    mgtserializer_class = MGTMajorTrackSerializer
    ecoserializer_class = ECOMajorTrackSerializer
    cseserializer_class = CSEMajorTrackSerializer


    def get_category_point(self, category_name):
        # category_name을 기반으로 포인트를 동적으로 설정
        student_year = self.request.user.student_year
        if student_year == 21 and category_name == '소프트웨어':
            return 0
        elif category_name == '서강인성':
            return 1
        elif category_name == '글쓰기':
            return 3
        elif category_name == '글로벌 언어I':
            return 3
        elif category_name == '전공 진로 탐색':
            return 1
        elif category_name == '소프트웨어':
            return 3
        # 나머지 경우에 대한 처리

    def get_queryset(self):
        student_year = self.request.user.student_year
        category_field_name = f"category{student_year}"
        category_names = ['서강인성', '글쓰기', '글로벌 언어I', '전공 진로 탐색', '소프트웨어']
        queryset = []
# #####################################
#         #student_year, track, major, submajor를 받아와서 채워줘야됨
#         track_pk = self.kwargs['track_pk']
#         major = self.request.user.major.title
#         if major == '경영':
#             points = MGTMajorTrack.objects.filter(track=track_pk).first()
#             queryset.append({
#                 'points': self.mgtserializer_class(points).data
#             })
#         elif major == '경제':
#             points = ECOMajorTrack.objects.filter(track=track_pk).first()
#             queryset.append({
#                 'points': self.ecoserializer_class(points).data
#             })
#         elif major == '컴퓨터공학':
#             points = CSEMajorTrack.objects.filter(track=track_pk).first()
#             queryset.append({
#                 'points': self.cseserializer_class(points).data
#             })
#         #만약 다전공이라면:
#         if major == '경영':
#             if track_pk == 1 or track_pk == 2 or track_pk == 3:

#         elif major == '경제':
#             if track_pk == 1 or track_pk == 2 or track_pk == 3:
#         elif major == '컴퓨터공학':
#             if track_pk == 3 or track_pk == 8 or track_pk == 13:


#         # track = CSETrack.objects.get(pk=track_pk)
#         # major_track = track.track_CSEtrack.first()
# #####################################
        for category_name in category_names:
            category_point = self.get_category_point(category_name)
            category = Category.objects.get(detail=category_name)

            if (self.request.user.major.title == '경영' or self.request.user.major.title == '경제') and category_name == '글쓰기':
                lectures = CommonLecture.objects.filter(
                    **{category_field_name: category, 'title': '인문사회글쓰기'}
                )
            elif self.request.user.major.title == '컴퓨터공학' and category_name == '글쓰기':
                lectures = CommonLecture.objects.filter(
                    **{category_field_name: category, 'title': '자연계글쓰기'}
                )
            elif self.request.user.major.title == '경영' and category_name == '전공 진로 탐색':
                lectures = CommonLecture.objects.filter(
                    **{category_field_name: category, 'title': '알바트로스세미나(경영)'}
                )
            elif (self.request.user.major.title == '경제' or self.request.user.major.title == '컴퓨터공학') and category_name == '전공 진로 탐색':
                lectures = CommonLecture.objects.filter(
                    **{category_field_name: category, 'title': '알바트로스세미나'}
                )
            else:
                lectures = CommonLecture.objects.filter(**{category_field_name: category})

            queryset.append({
                'category_detail': category_name,
                'category_point': category_point,
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
                **{category_field_name: category, 'title': '미적분학I'}  # 필터링 조건 추가
                )
            else:
                lectures = CommonLecture.objects.filter(**{category_field_name: category})
            
            queryset.append({
                'category_detail': category_name,
                'category_point': category_point,
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
    serializer_class = None

    def get_serializer_class(self):
        self.major = self.request.data.get('major') 
        if self.major == '경제':
            return ECOLectureDetailSerializer
        elif self.major == '컴퓨터공학':
            return CSELectureDetailSerializer
        elif self.major == '경영':
            return MGTLectureDetailSerializer
        elif self.major == '공통':
            return CommonLectureDetailSerializer

    def get_queryset(self):
        major = self.request.data.get('major', None)
        keyword = self.request.data.get('keyword',None)
        conditions = Q(title__icontains=keyword) if keyword else Q()

        if major:
            if major == '경제':
                return ECOLecture.objects.filter(conditions)
            elif major == '컴퓨터공학':
                return CSELecture.objects.filter(conditions)
            elif major == '경영':
                return MgtLecture.objects.filter(conditions)
            elif major == '공통':
                return CommonLecture.objects.filter(conditions)
            else:
                return []

    def list(self, request, *args, **kwargs):
        self.major = self.request.data.get('major')
        self.keyword = self.request.data.get('keyword')
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()

        if queryset and serializer_class:
            serializer = serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response([])





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

    def get_queryset(self):
        category_name = '전공입문교과'
        queryset = []
        user_request = self.request.user
        track_pk = self.kwargs['track_pk']
        track = CSETrack.objects.get(pk=track_pk)
        completed_lecture = UserCSELecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        if track.title == ('단일전공' or '융합과정'):
            if track.title=='단일전공':
                queryset.append({
                    'track': '단일전공',
                    '이수 학점': category_point
                })
            elif track.title=='융합과정':
                queryset.append({
                    'track': '융합과정',
                    '이수 학점': category_point
                })
            # 필수 과목
            duty_lectures = [
                '미적분학II', '일반물리실험I', '일반물리I', '응용수학I', '응용수학II'
            ]
            duty_category_point = 13
            filtered_duty_lectures = CSELecture.objects.filter(
                title__in=duty_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수',
                'category_point': duty_category_point,
                'lectures': self.serializer_class(filtered_duty_lectures, many=True).data
            })

            # 선택 과목
            choice_lectures = [
                '집합론', '선형대수학', '정수론'
            ]
            choice_category_point = 3

            filtered_choice_lectures = CSELecture.objects.filter(
                title__in=choice_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '선택',
                'category_point': choice_category_point,
                'lectures': self.serializer_class(filtered_choice_lectures, many=True).data
            })
        
        elif track.title == '다전공 1전공':
            queryset.append({
                'track': '다전공 1전공',
                '이수 학점': category_point
            })
            # 필수 과목
            duty_lectures = [
                '응용수학I', '응용수학II'
            ]
            duty_category_point = 6
            filtered_duty_lectures = CSELecture.objects.filter(
                title__in=duty_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수',
                'category_point': duty_category_point,
                'lectures': self.serializer_class(filtered_duty_lectures, many=True).data
            })
                
        elif track.title == '다전공 타전공':
            queryset.append({
                'track': '다전공 타전공',
                '이수 학점': category_point
            })
            # 필수 과목
            duty_lectures = [
                '고급응용C프로그래밍', '기초C언어'
            ]
            duty_category_point = 3
            filtered_duty_lectures = CSELecture.objects.filter(
                title__in=duty_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수',
                'category_point': duty_category_point,
                'lectures': self.serializer_class(filtered_duty_lectures, many=True).data
            })

        elif track.title == '교직과정':
            queryset.append({
                'track': '교직과정',
                '이수 학점': category_point
            })
            # 필수 과목
            duty_lectures = [
                '응용수학I', '응용수학II', '일반물리실험I', '일반물리I', '일반물리II'
            ]
            duty_category_point = 13
            filtered_duty_lectures = CSELecture.objects.filter(
                title__in=duty_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수',
                'category_point': duty_category_point,
                'lectures': self.serializer_class(filtered_duty_lectures, many=True).data
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
        category_name = '전공필수교과'
        queryset = []
        user_request = self.request.user
        track_pk = self.kwargs['track_pk']
        track = CSETrack.objects.get(pk=track_pk)
        completed_lecture = UserCSELecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        if track.title=='단일전공' or track.title=='융합과정' or track.title=='다전공 1전공':
            if track.title=='단일전공':
                queryset.append({
                    'track': '단일전공',
                    '이수 학점': category_point
                })
            elif track.title=='융합과정':
                queryset.append({
                    'track': '융합과정',
                    '이수 학점': category_point
                })
            elif track.title=='다전공 1전공':
                queryset.append({
                    'track': '다전공 1전공',
                    '이수 학점': category_point
                })
            # 필수 과목
            duty_lectures = [
                '컴퓨터프로그래밍I(구 기초공학설계)', '컴퓨터프로그래밍II(구 C프로그래밍)', '이산구조', '컴퓨터공학설계및실험I', '디지털회로개론', '컴퓨터공학실험II', '자료구조', '운영체제', '멀티코어 프로그래밍', '고급소프트웨어실습I', '캡스톤디자인II'
            ]
            duty_category_point = 33
            filtered_duty_lectures = CSELecture.objects.filter(
                title__in=duty_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수',
                'category_point': duty_category_point,
                'lectures': self.serializer_class(filtered_duty_lectures, many=True).data
            })

            # 선택 과목
            choice_lectures = [
                '캡스톤디자인I', '인턴쉽I'
            ]
            choice_category_point = 3

            filtered_choice_lectures = CSELecture.objects.filter(
                title__in=choice_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수선택',
                'category_point': choice_category_point,
                'lectures': self.serializer_class(filtered_choice_lectures, many=True).data
            })
        
        elif track.title == '다전공 타전공':
            queryset.append({
                'track': '다전공 타전공',
                '이수 학점': category_point
            })
            # 필수 과목
            duty_lectures = [
                '자료구조', '알고리즘설계와분석'
            ]
            duty_category_point = 6
            filtered_duty_lectures = CSELecture.objects.filter(
                title__in=duty_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수',
                'category_point': duty_category_point,
                'lectures': self.serializer_class(filtered_duty_lectures, many=True).data
            })

        elif track.title == '교직과정':
            queryset.append({
                'track': '교직과정',
                '이수 학점': category_point
            })
            # 필수 과목
            duty_lectures = [
                '컴퓨터프로그래밍I(구 기초공학설계)', '컴퓨터프로그래밍II(구 C프로그래밍)', '이산구조', '컴퓨터공학설계및실험I', '디지털회로개론', '컴퓨터공학실험II', '자료구조', '운영체제', '시스템프로그래밍', '고급소프트웨어실습I', '캡스톤디자인II', '컴퓨터교과교육론', '컴퓨터학교과교재연구및지도법', '컴퓨터학교과논리및논술'
            ]
            duty_category_point = 42
            filtered_duty_lectures = CSELecture.objects.filter(
                title__in=duty_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수',
                'category_point': duty_category_point,
                'lectures': self.serializer_class(filtered_duty_lectures, many=True).data
            })

            # 선택 과목
            choice_lectures = [
                '캡스톤디자인I', '인턴쉽I'
            ]
            choice_category_point = 3

            filtered_choice_lectures = CSELecture.objects.filter(
                title__in=choice_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수선택',
                'category_point': choice_category_point,
                'lectures': self.serializer_class(filtered_choice_lectures, many=True).data
            })

        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
    
class CSEDutyChoiceLectureListView(generics.ListAPIView):
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
        category_name = '전공선택교과'
        queryset = []
        user_request = self.request.user
        track_pk = self.kwargs['track_pk']
        track = CSETrack.objects.get(pk=track_pk)
        completed_lecture = UserCSELecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        category_except_name = '전공입문교과'
        category_except_detail_name1 = '필수'
        category_except_detail_name2 = '선택'
        category1 = Category.objects.filter(title=category_except_name, detail=category_except_detail_name1).first()
        category2 = Category.objects.filter(title=category_except_name, detail=category_except_detail_name2).first()
        if track.title == '단일전공':
            queryset.append({
                'track': '단일전공',
                '이수 학점': category_point
            })
            # 필수 과목
            duty_lectures = [
                '알고리즘설계와분석', '컴퓨터아키텍쳐', '프로그래밍언어', '데이터베이스시스템', '소프트웨어공학', '컴퓨터네트워크', '기초인공지능'
            ]
            duty_category_point = 12
            filtered_duty_lectures = CSELecture.objects.filter(
                title__in=duty_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수',
                'category_point': duty_category_point,
                'lectures': self.serializer_class(filtered_duty_lectures, many=True).data
            })

        elif track.title == '융합과정':
            queryset.append({
                'track': '융합과정',
                '이수 학점': category_point
            })
            # 필수 과목
            duty_lectures = [
                '알고리즘설계와분석', '컴퓨터아키텍쳐', '프로그래밍언어', '데이터베이스시스템', '소프트웨어공학', '컴퓨터네트워크', '기초인공지능'
            ]
            duty_category_point = 12
            filtered_duty_lectures = CSELecture.objects.filter(
                title__in=duty_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수',
                'category_point': duty_category_point,
                'lectures': self.serializer_class(filtered_duty_lectures, many=True).data
            })

        elif track.title == '다전공 1전공':
            queryset.append({
                'track': '다전공 1전공',
                '이수 학점': category_point
            })
            # 필수 과목
            duty_lectures = [
                '알고리즘설계와분석', '컴퓨터아키텍쳐', '프로그래밍언어', '데이터베이스시스템', '소프트웨어공학', '컴퓨터네트워크', '기초인공지능'
            ]
            duty_category_point = 12
            filtered_duty_lectures = CSELecture.objects.filter(
                title__in=duty_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수',
                'category_point': duty_category_point,
                'lectures': self.serializer_class(filtered_duty_lectures, many=True).data
            })

        elif track.title == '다전공 타전공':
            queryset.append({
                'track': '다전공 타전공',
                '이수 학점': category_point
            })
            # 필수 과목
            duty_system_lectures = [
                '컴퓨터아키텍쳐', '프로그래밍언어', '멀티코어 프로그래밍', '데이터베이스시스템', '컴퓨터네트워크'
            ]
            duty_system_point = 9
            filtered_duty_system_lectures = CSELecture.objects.filter(
                title__in=duty_system_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수_시스템 및 이론 그룹',
                'category_point': duty_system_point,
                'lectures': self.serializer_class(filtered_duty_system_lectures, many=True).data
            })
            
            duty_ai_lectures = [
                '소프트웨어공학', '기초머신러닝', '기초컴퓨터그래픽스', '기초인공지능', '암호학기초'
            ]
            duty_ai_point = 9
            filtered_duty_ai_lectures = CSELecture.objects.filter(
                title__in=duty_ai_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수_인공지능 및 응용 그룹',
                'category_point': duty_ai_point,
                'lectures': self.serializer_class(filtered_duty_ai_lectures, many=True).data
            })

        elif track.title == '교직과정':
            queryset.append({
                'track': '교직과정',
                '이수 학점': category_point
            })
            # 필수 과목
            duty_lectures = [
                '알고리즘설계와분석', '컴퓨터아키텍쳐', '프로그래밍언어', '데이터베이스시스템', '소프트웨어공학', '컴퓨터네트워크', '기초인공지능'
            ]
            duty_category_point = 12
            filtered_duty_lectures = CSELecture.objects.filter(
                title__in=duty_lectures,
            ).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '필수',
                'category_point': duty_category_point,
                'lectures': self.serializer_class(filtered_duty_lectures, many=True).data
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
        category_name = '전공선택교과'
        queryset = []
        user_request = self.request.user
        track_pk = self.kwargs['track_pk']
        track = CSETrack.objects.get(pk=track_pk)
        completed_lecture = UserCSELecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        category_except_name = '전공입문교과'
        category_except_detail_name1 = '필수'
        category_except_detail_name2 = '선택'
        category1 = Category.objects.filter(title=category_except_name, detail=category_except_detail_name1).first()
        category2 = Category.objects.filter(title=category_except_name, detail=category_except_detail_name2).first()
        if track.title == '단일전공':
            queryset.append({
                'track': '단일전공',
                '이수 학점': category_point
            })

            # 선택 과목
            choice_lectures = [] #**전체중에서 지금까지 담은 전공과목을 제외하고 남은 전공과목들인데 이는 프론트가 지금까지 담은 과목을 처리해줘야됨
            choice_category_point = 24
            filtered_choice_lectures = CSELecture.objects.exclude(**{category_field_name: category1}).exclude(**{category_field_name: category2}).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '선택',
                'category_point': choice_category_point,
                'lectures': self.serializer_class(filtered_choice_lectures, many=True).data
            })
        
        elif track.title == '융합과정':
            queryset.append({
                'track': '융합과정',
                '이수 학점': category_point
            })
            
            choice_lectures = [] #**전체중에서 지금까지 담은 전공과목을 제외하고 남은 전공과목들인데 이는 프론트가 지금까지 담은 과목을 처리해줘야됨
            choice_category_point = 12
            filtered_choice_lectures = CSELecture.objects.exclude(**{category_field_name: category1}).exclude(**{category_field_name: category2}).exclude(id__in=completed_lecture)
            # 융합과정은 타전공의 전공과목 중 한 전공 내에서만 21학점을 이수해야됨. 이걸 여기서 어떻게 처리를 해줘야될지가 관건

            queryset.append({
                'category_detail': '선택',
                'category_point': choice_category_point,
                'lectures': self.serializer_class(filtered_choice_lectures, many=True).data
            })

        elif track.title == '다전공 1전공':
            queryset.append({
                'track': '다전공 1전공',
                '이수 학점': category_point
            })

            # 선택 과목
            choice_lectures = [] #**전체중에서 지금까지 담은 전공과목을 제외하고 남은 전공과목들인데 이는 프론트가 지금까지 담은 과목을 처리해줘야됨
            choice_category_point = 12
            filtered_choice_lectures = CSELecture.objects.exclude(**{category_field_name: category1}).exclude(**{category_field_name: category2}).exclude(id__in=completed_lecture)
            queryset.append({
                'category_detail': '선택',
                'category_point': choice_category_point,
                'lectures': self.serializer_class(filtered_choice_lectures, many=True).data
            })

        elif track.title == '다전공 타전공':
            queryset.append({
                'track': '다전공 타전공',
                '이수 학점': category_point
            })

            # 선택 과목
            choice_lectures = [] #**전체중에서 지금까지 담은 전공과목을 제외하고 남은 전공과목들인데 이는 프론트가 지금까지 담은 과목을 처리해줘야됨
            choice_category_point = 15
            filtered_choice_lectures = CSELecture.objects.exclude(**{category_field_name: category1}).exclude(**{category_field_name: category2}).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '선택',
                'category_point': choice_category_point,
                'lectures': self.serializer_class(filtered_choice_lectures, many=True).data
            })

        elif track.title == '교직과정':
            queryset.append({
                'track': '교직과정',
                '이수 학점': category_point
            })

            # 선택 과목
            choice_lectures = [] #**전체중에서 지금까지 담은 전공과목을 제외하고 남은 전공과목들인데 이는 프론트가 지금까지 담은 과목을 처리해줘야됨
            choice_category_point = 3
            filtered_choice_lectures = CSELecture.objects.exclude(**{category_field_name: category1}).exclude(**{category_field_name: category2}).exclude(id__in=completed_lecture)

            queryset.append({
                'category_detail': '선택',
                'category_point': choice_category_point,
                'lectures': self.serializer_class(filtered_choice_lectures, many=True).data
            })

        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
# class CSEDutyLectureListView(generics.ListAPIView):
#     serializer_class = CSELectureDetailSerializer

#     # 프론트로부터 user가 고른 track의 pk를 받아서, related_name을 통해서 track_CSEtrack을 통해서 각 category_point를 불러옴.
#     def get_category_point(self, category_name):
#         track_pk = self.kwargs['track_pk']
#         track = CSETrack.objects.get(pk=track_pk)
#         major_track = track.track_CSEtrack.first()  # 첫 번째 MajorTrack을 선택합니다.
#         if major_track is not None:
#             return major_track.duty_point
#         else:
#             return None  # 또는 적절한 디폴트값을 반환할 수 있습니다.

#     def get_queryset(self):
#         student_year = self.request.user.student_year
#         category_field_name = f"category{student_year}"
#         print(category_field_name)
#         category_name = '전공필수교과'
#         category_details = ['']
#         queryset = []
#         user_request = request.user
#         completed_lecture = UserCSELecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
#         category_point = self.get_category_point(category_name)
#         categories = Category.objects.filter(title=category_name)  # Use filter instead of get
#         for category in categories:
            
#             # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
#             lectures = CSELecture.objects.filter(**{category_field_name: category}).exclude(id__in=completed_lecture)
#             queryset.append({
#                 category.detail: category_point,
#                 'lectures': self.serializer_class(lectures, many=True).data
#             })

#         return queryset

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         return Response(queryset)


# class CSEChoiceLectureListView(generics.ListAPIView):
#     serializer_class = CSELectureDetailSerializer

#     # 프론트로부터 user가 고른 track의 pk를 받아서, related_name을 통해서 track_CSEtrack을 통해서 각 category_point를 불러옴.
#     def get_category_point(self, category_name):
#         track_pk = self.kwargs['track_pk']
#         track = CSETrack.objects.get(pk=track_pk)
#         major_track = track.track_CSEtrack.first()  # 첫 번째 MajorTrack을 선택합니다.
#         if major_track is not None:
#             return major_track.choice_point
#         else:
#             return None  # 또는 적절한 디폴트값을 반환할 수 있습니다.

#     def get_queryset(self):
#         student_year = self.request.user.student_year
#         category_field_name = f"category{student_year}"
#         print(category_field_name)
#         category_name = '전공선택교과'
#         category_details = ['']
#         queryset = []
#         user_request = request.user
#         completed_lecture = UserCSELecture.objects.filter(user=user_request).values_list('cselecture_id', flat=True)
#         category_point = self.get_category_point(category_name)
#         categories = Category.objects.filter(title=category_name)  # Use filter instead of get
#         for category in categories:
            
#             # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
#             lectures = CSELecture.objects.filter(**{category_field_name: category}).exclude(id__in=completed_lecture)
#             queryset.append({
#                 category.detail: category_point,
#                 'lectures': self.serializer_class(lectures, many=True).data
#             })

#         return queryset


#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         return Response(queryset)
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
        category_name = '전공입문교과'
        queryset = []
        user_request = self.request.user
        track_pk = self.kwargs['track_pk']
        track = MGTTrack.objects.get(pk=track_pk)
        completed_lecture = UserMGTLecture.objects.filter(user=user_request).values_list('mgtlecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        queryset.append({
                    'track': 'all',
                    '이수 학점': category_point
                })
        choice_lectures_1 = [
                '경제학원론 I', '경제학원론 II'
            ]
        choice_1_category_point = 3
        filtered_choice_lectures_1 = MGTLecture.objects.filter(
                title__in=choice_lectures_1,
            ).exclude(id__in=completed_lecture)
        queryset.append({
                'category_detail': '선택1',
                'category_point': choice_1_category_point,
                'lectures': self.serializer_class(filtered_choice_lectures_1, many=True).data
            })
        choice_lectures_2 = [
                '경영통계학', '경제통계학', '통계학입문', '응용수학I'
            ]
        choice_2_category_point = 3
        filtered_choice_lectures_2 = MGTLecture.objects.filter(
                title__in=choice_lectures_2,
            ).exclude(id__in=completed_lecture)
        queryset.append({
                'category_detail': '선택2',
                'category_point': choice_2_category_point,
                'lectures': self.serializer_class(filtered_choice_lectures_2, many=True).data
            })
        choice_lectures_3 = [
                '대학수학', '미적분학I', '미적분II'
            ]
        choice_3_category_point = 3
        filtered_choice_lectures_3 = MGTLecture.objects.filter(
                title__in=choice_lectures_3,
            ).exclude(id__in=completed_lecture)
        queryset.append({
                'category_detail': '선택3',
                'category_point': choice_3_category_point,
                'lectures': self.serializer_class(filtered_choice_lectures_3, many=True).data
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
        category_name = '전공필수교과'
        queryset = []
        user_request = self.request.user
        completed_lecture = UserMGTLecture.objects.filter(user=user_request).values_list('mgtlecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        category = Category.objects.filter(title=category_name).first()  # Use filter instead of get
        lectures = MGTLecture.objects.filter(**{category_field_name: category}).exclude(id__in=completed_lecture)
        queryset.append({
                    'track': 'all',
                    '이수 학점': category_point
                })
        queryset.append({
                        'category_detail': None,
                        'category_point': category_point,
                        'lectures': self.serializer_class(lectures, many=True).data
                    })
        # categories = Category.objects.filter(title=category_name)  # Use filter instead of get
        # for category in categories:
        #     major_techs = MGTTech.objects.all()
        #     for major_tech in major_techs:
        #     # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
        #         lectures = MGTLecture.objects.filter(**{category_field_name: category}, tech=major_tech).exclude(id__in=completed_lecture)
        #         if lectures.exists():  # Check if there are any lectures for this combination
        #             queryset.append({
        #                 'major_tech_title': major_tech.title,
        #                 'category_point': category_point,
        #                 'lectures': self.serializer_class(lectures, many=True).data
        #             })

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
    
class MGTDutyChoiceLectureListView(generics.ListAPIView):
    serializer_class = MGTLectureDetailSerializer

    # 프론트로부터 user가 고른 track의 pk를 받아서, related_name을 통해서 track_CSEtrack을 통해서 각 category_point를 불러옴.
    def get_category_point(self, category_name):
        track_pk = self.kwargs['track_pk']
        track = MGTTrack.objects.get(pk=track_pk)
        major_track = track.track_MGTtrack.first()  # 첫 번째 MajorTrack을 선택합니다.
        if major_track is not None:
            return major_track.duty_choice_point
        else:
            return None  # 또는 적절한 디폴트값을 반환할 수 있습니다.

    def get_queryset(self):
        student_year = self.request.user.student_year
        category_field_name = f"category{student_year}"
        print(category_field_name)
        category_name = '전공선택교과'
        category_detail = '필수'
        queryset = []
        user_request = self.request.user
        completed_lecture = UserMGTLecture.objects.filter(user=user_request).values_list('mgtlecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        queryset.append({
                    'track': 'all',
                    '이수 학점': category_point
                })
        categories = Category.objects.filter(title=category_name, detail=category_detail)  # Use filter instead of get
        for category in categories:
            major_techs = MGTTech.objects.all()
            for major_tech in major_techs:
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
    
class MGTChoiceLectureListView(generics.ListAPIView):  ## 남은걸 뽑아줘야됨
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
        category_name = '전공선택교과'
        category_detail = '선택'
        queryset = []
        user_request = self.request.user
        completed_lecture = UserMGTLecture.objects.filter(user=user_request).values_list('mgtlecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        queryset.append({
                    'track': 'all',
                    '이수 학점': category_point
                })
        category_except_name = '전공입문교과'
        category_except_detail_name = '선택'
        category = Category.objects.filter(title=category_except_name, detail=category_except_detail_name).first()  # Use filter instead of get
        major_techs = MGTTech.objects.all()
        for major_tech in major_techs:
            lectures = MGTLecture.objects.filter(tech=major_tech).exclude(**{category_field_name: category}).exclude(id__in=completed_lecture)
            if lectures.exists():  # Check if there are any lectures for this combination
                queryset.append({
                    'major_tech_title': major_tech.title,
                    'lectures': self.serializer_class(lectures, many=True).data
                })
        lectures = MGTLecture.objects.filter(tech=None).exclude(**{category_field_name: category}).exclude(id__in=completed_lecture)
        queryset.append({
                    'major_tech_title': 'null',
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
        category_name = '전공입문교과'
        queryset = []
        user_request = self.request.user
        track_pk = self.kwargs['track_pk']
        track = ECOTrack.objects.get(pk=track_pk)
        completed_lecture = UserECOLecture.objects.filter(user=user_request).values_list('ecolecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        queryset.append({
                    'track': 'all',
                    '이수 학점': category_point
                })
        duty_lectures = [
                '회계학원론'
            ]
        duty_category_point = 3
        filtered_choice_lectures_1 = ECOLecture.objects.filter(
                title__in=duty_lectures,
            ).exclude(id__in=completed_lecture)
        queryset.append({
                'category_detail': '필수',
                'category_point': duty_category_point,
                'lectures': self.serializer_class(filtered_choice_lectures_1, many=True).data
            })
        choice_lectures = [
                '경제수리기초', '미적분학 I', '미적분학 II'
            ]
        choice_category_point = 3
        filtered_choice_lectures_2 = ECOLecture.objects.filter(
                title__in=choice_lectures,
            ).exclude(id__in=completed_lecture)
        queryset.append({
                'category_detail': '선택',
                'category_point': choice_category_point,
                'lectures': self.serializer_class(filtered_choice_lectures_2, many=True).data
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
        category_name = '전공필수교과'
        queryset = []
        user_request = self.request.user
        completed_lecture = UserECOLecture.objects.filter(user=user_request).values_list('ecolecture_id', flat=True)
        category_point = self.get_category_point(category_name)
        category = Category.objects.filter(title=category_name).first()  # Use filter instead of get
        lectures = ECOLecture.objects.filter(**{category_field_name: category}).exclude(id__in=completed_lecture)
        queryset.append({
                    'track': 'all',
                    '이수 학점': category_point
                })
        queryset.append({
                        'category_detail': None,
                        'category_point': category_point,
                        'lectures': self.serializer_class(lectures, many=True).data
                    })
    # def get_queryset(self):
    #     student_year = self.request.user.student_year
    #     category_field_name = f"category{student_year}"
    #     category_name = '전공필수교과'
    #     category_details = ['']
    #     queryset = []
    #     user_request = self.request.user #self.request.user 일수도
    #     completed_lecture = UserECOLecture.objects.filter(user=user_request).values_list('ecolecture_id', flat=True)
    #     category_point = self.get_category_point(category_name)
    #     categories = Category.objects.filter(title=category_name)  # Use filter instead of get
    #     for category in categories:
    #         major_techs = ECOTech.objects.all()
    #         for major_tech in major_techs:
    #         # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
    #             lectures = ECOLecture.objects.filter(**{category_field_name: category}).exclude(id__in=completed_lecture)
    #             if lectures.exists():  # Check if there are any lectures for this combination
    #                 queryset.append({
    #                     'major_tech_title': major_tech.title,
    #                     'lectures': self.serializer_class(lectures, many=True).data
    #                 })

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)


class ECODutyChoiceLectureListView(generics.ListAPIView):
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
        
        user_request = self.request.user
        track_pk = self.kwargs['track_pk']
        track = ECOTrack.objects.get(pk=track_pk)
        completed_lecture = UserECOLecture.objects.filter(user=user_request).values_list('ecolecture_id', flat=True)
        queryset = []
        # if track.title == '단일전공':
        #     category_point = 27
        # else:
        #     category_point = 21
        category_point = 12
        queryset.append({
                    'track': track.title,
                    '이수 학점': category_point
                })
        # queryset.append({
        #             '금융경제 필수': 3,
        #             '금융경제 선택 필수': 9,
        #             '글로벌경제 필수': 6,
        #             '글로벌경제 선택 필수': 6,
        #             '계량경제 필수': 3,
        #             '계량경제 선택 필수': 9,
        #             '산업경제 필수': 3,
        #             '산업경제 선택 필수': 9,
        #             '공공경제 필수': 3,
        #             '공공경제 선택 필수': 9
        #         })
        
        major_techs = ECOTech.objects.all()
        for major_tech in major_techs:
            lectures = ECOLecture.objects.filter(tech=major_tech).exclude(id__in=completed_lecture)
            duty_lectures = lectures.filter(**{f"{category_field_name}__detail": '필수'})
            duty_choice_lectures = lectures.filter(**{f"{category_field_name}__detail": '선택 필수'})
            if major_tech.title == '글로벌경제':
                duty_point = 6
                duty_choice_point = 6
            else:
                duty_point = 3
                duty_choice_point = 9
            if lectures.exists():  # Check if there are any lectures for this combination
                    queryset.append({
                        'major_tech_title': major_tech.title,
                        'duty_point': duty_point,
                        'duty_lectures': self.serializer_class(duty_lectures, many=True).data,
                        'duty_choice_point': duty_choice_point,
                        'duty_choice_lectures': self.serializer_class(duty_choice_lectures, many=True).data
                    })
        # lectures = ECOLecture.objects.filter(tech=None).exclude(id__in=completed_lecture)
        # choice_lectures = lectures.filter(**{f"{category_field_name}__title": '전공선택교과'})
        # queryset.append({
        #     'major_tech_title': 'None',
        #     'choice_lectures': self.serializer_class(choice_lectures, many=True).data
        # })
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
    
    
        # category_name = '전공선택교과'
        # category_details = ['']
        # queryset = []
        # user_request = request.user #self.request.user 일수도
        # completed_lecture = UserECOLecture.objects.filter(user=user_request).values_list('ecolecture_id', flat=True)
        # category_point = self.get_category_point(category_name)
        # categories = Category.objects.filter(title=category_name)  # Use filter instead of get
        # for category in categories:
        #     major_techs = MajorTech.objects.all()
        #     for major_tech in major_techs:
        #     # 프론트측에서 이미 앞서 공통에서 미적분학을  담았을때, 미적분학은 안담게하고 3학점은 올라가있게 해놔야됨.
        #         lectures = ECOLecture.objects.filter(**{category_field_name: category}, tech=major_tech).exclude(id__in=completed_lecture)
        #         if lectures.exists():  # Check if there are any lectures for this combination
        #             queryset.append({
        #                 'major_tech_title': major_tech.title,
        #                 'lectures': self.serializer_class(lectures, many=True).data
        #             })
class ECOChoiceLectureListView(generics.ListAPIView):  ## 남은걸 뽑아줘야됨
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
        category_name = '전공선택교과'
        category_detail = '선택'
        queryset = []
        user_request = self.request.user
        track_pk = self.kwargs['track_pk']
        track = ECOTrack.objects.get(pk=track_pk)
        completed_lecture = UserECOLecture.objects.filter(user=user_request).values_list('ecolecture_id', flat=True)
        if track.title == '단일전공':
            category_point = 15
        else:
            category_point = 9
        queryset.append({
                    'track': 'all',
                    '이수 학점': category_point
                })
        category_except_name = '전공입문교과'
        category_except_detail_name = '선택'
        category = Category.objects.filter(title=category_except_name, detail=category_except_detail_name).first()  # Use filter instead of get
        major_techs = ECOTech.objects.all()
        for major_tech in major_techs:
            lectures = ECOLecture.objects.filter(tech=major_tech).exclude(**{category_field_name: category}).exclude(id__in=completed_lecture)
            if lectures.exists():  # Check if there are any lectures for this combination
                queryset.append({
                    'major_tech_title': major_tech.title,
                    'lectures': self.serializer_class(lectures, many=True).data
                })
        lectures = ECOLecture.objects.filter(tech=None).exclude(**{category_field_name: category}).exclude(id__in=completed_lecture)
        queryset.append({
                    'major_tech_title': 'null',
                    'lectures': self.serializer_class(lectures, many=True).data
                })
    
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset)
####################################################################################################################################################333
# 로드맵 디테일 생성하기 작성
class RoadmapDetailCreateView(generics.CreateAPIView):
    serializer_class = RoadmapDetailCreateSerializers
    queryset = RoadmapDetail.objects.all()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Assuming the title is provided in the request data
        
        roadmap_id = serializer.validated_data.get('roadmap').id
        
        # Assuming you're using the authenticated user
        user = request.user
        roadmap =Roadmap.objects.get(pk = roadmap_id)
        semester_count = RoadmapDetail.objects.filter(roadmap=roadmap, semester__contains="추가학기").count()
        i =semester_count+1
        semester = f"추가학기{i}"
        # Create the Roadmap
        roadmapdetail = RoadmapDetail.objects.create(
            semester = semester,
            
            roadmap = roadmap
            
        )

        return Response({'id': roadmapdetail.id}, status=status.HTTP_201_CREATED)
        

# 로드맵 디테일 이름 변경 또는 추가 또는 삭제
class RoadmapDetailUpdateDeleteView(APIView):
    def delete(self, request, pk, format=None):
        try:
            roadmap_detail = RoadmapDetail.objects.get(pk=pk)
            roadmap_detail.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RoadmapDetail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            roadmap_detail = RoadmapDetail.objects.get(pk=pk)
            serializer = RoadmapDetailSerializers(roadmap_detail, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except RoadmapDetail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class RoadmapDetailCreateAPIView(generics.CreateAPIView):
    queryset = RoadmapDetail.objects.all()
# 로드맵 수정 및 만들어주기
class RoadmapUpdateDeleteView(APIView):
    def delete(self, request, pk, format=None):
        try:
            roadmap_detail = Roadmap.objects.get(pk=pk)
            roadmap_detail.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Roadmap.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            user = request.user
            roadmap_detail = Roadmap.objects.get(pk=pk, student=user)
            serializer = RoadmapsSerializers(roadmap_detail, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Roadmap.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RoadmapCreateAPIView(generics.CreateAPIView):
    queryset = Roadmap.objects.all()
    serializer_class = RoadMapSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Assuming the title is provided in the request data
        title = serializer.validated_data.get('title')

        # Assuming you're using the authenticated user
        user = request.user

       

        # Create the Roadmap
        roadmap = Roadmap.objects.create(
            student=user,
            title=title
        )

        return Response({'id': roadmap.id}, status=status.HTTP_201_CREATED)
#########################################################################################
# 로드맵에 과목 넣어주기 ()
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
# 이수한 놈들 추가할 수 있는 코드(completed=True로 만들어주고 action에 따라 달라짐)
class CompletedLectureCreateView(APIView):
    def post(self, request, format=None):
        action = request.data.get('action')
        
        if action == 'add_roadmap_lecture':
            serializer = RoadmapDetailLectureCreateSerializer(data=request.data)
            create_method = self.create_roadmap_lecture
        elif action == 'add_completed_lecture':
            serializer = CompletedLectureCreateSerializer(data=request.data)
            create_method = self.create_completed_lecture
        else:
            return Response({"error": "Invalid action."}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            return create_method(serializer)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def create_roadmap_lecture(self, serializer):
        roadmap_detail_id = serializer.validated_data.get('roadmap_detail_id')
        lecture_type = serializer.validated_data.get('lecture_type')
        lecture_id = serializer.validated_data.get('lecture_id')
        
        try:
            if lecture_type == 'commonlecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                commonlecture = CommonLecture.objects.get(pk=lecture_id)
                obj = RoadmapDetailLecture.objects.create(
                    completed = True,
                    roadmap_detail=roadmap_detail,
                    commonlecture=commonlecture
                )
            elif lecture_type == 'cselecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                cselecture = CSELecture.objects.get(pk=lecture_id)
                obj = RoadmapDetailLecture.objects.create(
                    completed = True,
                    roadmap_detail=roadmap_detail,
                    cselecture=cselecture
                )
            elif lecture_type == 'ecolecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                ecolecture = ECOLecture.objects.get(pk=lecture_id)
                obj = RoadmapDetailLecture.objects.create(
                    completed = True,
                    roadmap_detail=roadmap_detail,
                    ecolecture=ecolecture
                )
            elif lecture_type == 'mgtlecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                commonlecture = MGTLecture.objects.get(pk=lecture_id)
                obj = RoadmapDetailLecture.objects.create(
                    completed = True,
                    roadmap_detail=roadmap_detail,
                    commonlecture=commonlecture
                )
            else:
                raise serializers.ValidationError("Invalid lecture type")

            return Response(serializer.data, status=status.HTTP_201_CREATED)

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

    def create_completed_lecture(self, serializer):
        user_id = self.request.user
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
                mgtlecture = MGTLecture.objects.get(pk=lecture_id)
                obj = UserMGTLecture.objects.create(
                    user=user_id,
                    mgtlecture = mgtlecture
                )
            else:
                raise serializers.ValidationError("Invalid lecture type")

            return Response({"message": "Object created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)

        except CommonLecture.DoesNotExist as e:
            return Response({"error": f"CommonLecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        except CSELecture.DoesNotExist as e:
            return Response({"error": f"CSELecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        except ECOLecture.DoesNotExist as e:
            return Response({"error": f"ECOLecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        except MGTLecture.DoesNotExist as e:
            return Response({"error": f"MGTLecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)
#################################################################################
# 렉쳐 넣은 것들 수정하기 위해서 삭제하기
class RoadmapDetailLectureDeleteAPIView(generics.DestroyAPIView):
    def destroy(self, request, *args, **kwargs):


        roadmap_detail_id = request.data.get('roadmap_detail_id')
        lecture_type = request.data.get('lecture_type')
        lecture_id = request.data.get('lecture_id')
        try:
            if lecture_type == 'commonlecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                commonlecture = CommonLecture.objects.get(pk=lecture_id)
                obj = RoadmapDetailLecture.objects.filter(roadmap_detail=roadmap_detail, commonlecture=commonlecture)
                obj.delete()
            elif lecture_type == 'cselecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                cselecture = CSELecture.objects.get(pk=lecture_id)
                obj = RoadmapDetailLecture.objects.filter(roadmap_detail=roadmap_detail, cselecture=cselecture)
                
                obj.delete()
            elif lecture_type == 'ecolecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                ecolecture = ECOLecture.objects.get(pk=lecture_id)
                obj = RoadmapDetailLecture.objects.filter(roadmap_detail=roadmap_detail, ecolecture=ecolecture)
                
                obj.delete()
            elif lecture_type == 'mgtlecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                mgtlecture = MGTLecture.objects.get(pk=lecture_id)
                obj = RoadmapDetailLecture.objects.filter(roadmap_detail=roadmap_detail, mgtlecture=mgtlecture)
                
                obj.delete()
            
            return Response({"message": f"Lecture with id {lecture_id} deleted successfully."}, status=status.HTTP_200_OK)
        except RoadmapDetailLecture.DoesNotExist as e:
            return Response({"error": f"Lecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)
##################################################################################################################################
class CompletedLectureDeleteView(generics.DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        roadmap_detail_id = request.data.get('roadmap_detail_id')
        lecture_type = request.data.get('lecture_type')
        lecture_id = request.data.get('lecture_id')
        try:
            if lecture_type == 'commonlecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                commonlecture = CommonLecture.objects.get(pk=lecture_id)
                obj = RoadmapDetailLecture.objects.filter(roadmap_detail=roadmap_detail, commonlecture=commonlecture)
                user_obj = UserCommonLecture.objects.filter(user=request.user, commonlecture=commonlecture)
                user_obj.delete()
                obj.delete()
                user_obj = UserCommonLecture.objects.filter(user=request.user, commonlecture=commonlecture)
            elif lecture_type == 'cselecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                cselecture = CSELecture.objects.get(pk=lecture_id)
                obj = RoadmapDetailLecture.objects.filter(roadmap_detail=roadmap_detail, cselecture=cselecture)
                user_obj = UserCSELecture.objects.filter(user=request.user, cselecture=cselecture)
                user_obj.delete()
                obj.delete()
            elif lecture_type == 'ecolecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                ecolecture = ECOLecture.objects.get(pk=lecture_id)
                obj = RoadmapDetailLecture.objects.filter(roadmap_detail=roadmap_detail, ecolecture=ecolecture)
                user_obj = UserECOLecture.objects.filter(user=request.user, ecolecture=ecolecture)
                user_obj.delete()
                obj.delete()
            elif lecture_type == 'mgtlecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                mgtlecture = MGTLecture.objects.get(pk=lecture_id)
                obj = RoadmapDetailLecture.objects.filter(roadmap_detail=roadmap_detail, mgtlecture=mgtlecture)
                user_obj = UserMGTLecture.objects.filter(user=request.user, mgtlecture=mgtlecture)
                user_obj.delete()
                obj.delete()
            
            return Response({"message": f"Lecture with id {lecture_id} deleted successfully."}, status=status.HTTP_200_OK)
        except RoadmapDetailLecture.DoesNotExist as e:
            return Response({"error": f"Lecture with id {lecture_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)

############################################################################################################################################
class Roadmap_Roadmapdetail_CreatedAPIView(generics.CreateAPIView):
    queryset = Roadmap.objects.all()
    serializer_class = RoadMapSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)



        # Assuming you're using the authenticated user
        user = request.user
        roadmaps_count = Roadmap.objects.filter(student=user).count()
        
        new_title = f"#{roadmaps_count + 1}"
        # Create the Roadmap
        roadmap = Roadmap.objects.create(
            student=user,
            title=new_title
        )

        # Create RoadmapDetails
        titles = ['1-1', '1-하계','1-2','1-동계', '2-1', '2-하계', '2-2','2-동계', '3-1','3-하계', '3-2','3-동계' , '4-1','4-하계', '4-2','4-동계']
        for title in titles:
            RoadmapDetail.objects.create(
                semester=title,
                roadmap=roadmap
            )

        return Response({'id': roadmap.id}, status=status.HTTP_201_CREATED)