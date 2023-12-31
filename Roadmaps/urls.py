from django.urls import path, include
from .views import *


urlpatterns = [
    path('check/', checking.as_view()),
    path('',RoadmapFullView.as_view() ),
    path('default/',RoadmapDefaultView.as_view()),
    #디폴트값 넣어줄 로드맵이랑 로드맵 디테일 만들기
    path('default_roadmap_create/', Default_Roadmap_Roadmapdetail_CreatedAPIView.as_view()),
############################################################################################################################################################
    path('usermajortracks/',TrackByMajor.as_view()),
    path('pointslists/<int:track_pk>/<str:submajor>/',PointsListView.as_view()),
    path('commondutylecturelists/',CommonDutyLectureListView.as_view()),
    path('commonchoicelecturelists/',CommonChoiceLectureListView.as_view()),
############################################################################################################################################################
    path('completed_lecture_search/<str:major>/<str:search>/',CompletedSearchListAPIView.as_view() ),
    ############################################################################################################################
    path('cse_gicho_lecture/<int:track_pk>/' , CSEGichoLectureListView.as_view()),
    path('cse_duty_lecture/<int:track_pk>/' , CSEDutyLectureListView.as_view()),
    path('cse_duty_choice_lecture/<int:track_pk>/' , CSEDutyChoiceLectureListView.as_view()),
    path('cse_choice_lecture/<int:track_pk>/' , CSEChoiceLectureListView.as_view()),
    path('mgt_gicho_lecture/<int:track_pk>/' , MGTGichoLectureListView.as_view()),
    path('mgt_duty_lecture/<int:track_pk>/' , MGTDutyLectureListView.as_view()),
    path('mgt_duty_choice_lecture/<int:track_pk>/' , MGTDutyChoiceLectureListView.as_view()),
    path('mgt_choice_lecture/<int:track_pk>/' , MGTChoiceLectureListView.as_view()),
    path('eco_gicho_lecture/<int:track_pk>/' , ECOGichoLectureListView.as_view()),
    path('eco_duty_lecture/<int:track_pk>/' , ECODutyLectureListView.as_view()),
    path('eco_duty_choice_lecture/<int:track_pk>/' , ECODutyChoiceLectureListView.as_view()),
    path('eco_choice_lecture/<int:track_pk>/' , ECOChoiceLectureListView.as_view()),
    ###########################################################################33
    # 로드맵 만들고 자동으로 로드맵디테일 생성 (ㅇ)
    path('roadmap_roadmapdetail_create/', Roadmap_Roadmapdetail_CreatedAPIView.as_view()),
    # 로드 맵 디테일 생성 (ㅇ)
    path('roadmapdetail_create/', RoadmapDetailCreateView.as_view()),
    # 로드맵 디테일 수정해주고 삭제함 (ㅇ)
    path('roadmapdetail_update_delete/<int:pk>/', RoadmapDetailUpdateDeleteView.as_view(), name='create_roadmap_details'),
    # 로드맵 수정해주고 삭제함 (ㅇ)
    path('roadmap_update_delete/<int:pk>/', RoadmapUpdateDeleteView.as_view(), name='create_roadmap_details'),
    ##############################################################################################################
    # 로드맵 디테일 렉처에 과목들 넣어줌 그리고 삭제도 해줌 (업데이트 시)
    path('roadmapdetaillecture_create/', RoadmapDetailLectureCreateView.as_view(), name='create_roadmap_detail_lecture'),
    path('roadmapdetaillecture_create/delete/', RoadmapDetailLectureDeleteAPIView.as_view(), name='create_roadmap_detail_lecture'),

    # 이수 과목들 등록해줌
    path('completed_lecture_create/', CompletedLectureCreateView.as_view(), name='create_roadmap_detail_lecture'),
    path('completed_lecture_create/delete/', CompletedLectureDeleteView.as_view(), name='create_roadmap_detail_lecture'),
    
    # roadmap생성시 default값 적용되도록 함
    path('default_adjust/',Default_Adjust.as_view(), name='default_adjust' ),

    
]