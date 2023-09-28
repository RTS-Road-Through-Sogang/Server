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
# #class CategoryCommonLectureListView(generics.ListAPIView):
# #     serializer_class = CategoryCommonLecturesSerializer()

# #     def get_queryset(self):
# #         # URL 매개변수로 전달된 category_detail 값을 가져옵니다.
# #         category_detail = self.kwargs['category_detail']

# #         # Category 모델에서 detail 필드 값이 category_detail과 일치하는 카테고리를 가져옵니다.
# #         category = Category.objects.get(detail=category_detail)
# #         print(category_detail)
# #         # 해당 카테고리에 속하는 CommonLecture 데이터를 가져와서 반환합니다.
# #         common_lectures = CommonLecture.objects.filter(category23__detail=category.detail)
        
# #         return common_lectures
# # class CategoryCommonLecturesView(generics.ListAPIView):
# #     serializer_class = CategoryCommonLecturesSerializer

#     def get_queryset(self):
#         # URL에서 pk 값을 가져옵니다.
#         pk = self.kwargs.get('pk')
        
#         # pk를 사용하여 사용자의 student_year를 가져옵니다.
#         student_year = self.get_student_year(pk)  # 사용자 모델 및 필드 이름에 따라 조정 필요

#         # 동적으로 필드 이름을 생성합니다.
#         category_field_name = f'category{student_year}'

#         # 이제 category_field_name을 사용하여 필요한 필드를 필터링하여 반환합니다.
#         try:
#             category = Category.objects.get(detail='서강인성')
#         except Category.DoesNotExist:
#             category = None

#         if category:
#             commonlectures = CommonLecture.objects.filter(**{category_field_name: category})
#         else:
#             commonlectures = CommonLecture.objects.none()

#         return commonlectures

#     def get_student_year(self, pk):
#         # pk를 사용하여 사용자를 가져옵니다.
#         user = MyUser.objects.get(pk=pk)  # 사용자 모델에 따라 조정 필요

#         # 사용자 모델에서 student_year 필드를 가져옵니다.
#         student_year = user.student_year  # 사용자 모델 및 필드 이름에 따라 조정 필요

#         return student_year
#     serializer_class = CategoryGroupSerializer  # 사용할 시리얼라이저 클래스 지정

#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         user = MyUser.objects.get(student_number=user_id)
#         category_field_name = f"category{user.student_year}"
#         # 필요한 데이터를 쿼리합니다.
#         # 예: 공통 필수 교과목, 공통 선택 교과목에 해당하는 데이터를 가져옵니다.
#         common_duty_lectures = CommonLecture.objects.filter(category_field_name=)  # 필터링 조건을 지정하세요
#         common_choice_lectures = CommonLecture.objects.filter(...)  # 필터링 조건을 지정하세요

#         # 필터링된 데이터를 반환합니다.
#         return {
#             '공통 필수 교과': common_duty_lectures,
#             '공통 선택 교과': common_choice_lectures,
#         }
    
#     def list(self, request, *args, **kwargs):
#         # get_queryset()에서 반환된 데이터를 시리얼라이즈합니다.
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset)

#         # JSON 형식으로 응답합니다.
#         return Response(serializer.data)

# 2. 프론트로부터 고른 track과 다전공일때의 부전공을 받았을때 부전공이 null인지 1개인지 2개인지를 확인.

############################################################################################################################################################
class DoneLectures(generics.ListAPIView):
    serializer_class = alllectures
    def get_qeuryset(self):
        user_request = request.user
        completed_lecture = UserCommonLecture.objects.filter(user=user_request).values_list('commonlecture_id', flat=True)
        uncompleted_lectures = CommonLecture.objects.exclude(id__in=completed_lecture)
        search_keyword = self.request.query_params.get('title', None)
        if search_keyword is not None:
            uncompleted_lectures = uncompleted_lectures.filter(title__icontains=search_keyword)
        return uncompleted_lectures