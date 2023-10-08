from django.urls import path, include
from .views import *


urlpatterns = [
    path('',RoadmapFullView.as_view() ),
    path('fault/',RoadmapDefaultView.as_view()),
############################################################################################################################################################
    path('usermajortracks/',TrackByMajor.as_view()),
    path('commondutylecturelists/',CommonDutyLectureListView.as_view()),
    path('commonchoicelecturelists/',CommonChoiceLectureListView.as_view()),
############################################################################################################################################################
    path('completed_lecture/',CompletedSerachListAPIView.as_view() ),
    ############################################################################################################################
    path('cse_gicho_lecture/<int:track_pk>/' , CSEGichoLectureListView.as_view()),
    path('cse_choice_lecture/<int:track_pk>/' , CSEChoiceLectureListView.as_view()),
    path('cse_duty_lecture/<int:track_pk>/' , CSEDutyLectureListView.as_view()),
    path('mgt_gicho_lecture/<int:track_pk>/' , MGTGichoLectureListView.as_view()),
    path('mgt_duty_choice_lecture/<int:track_pk>/' , MGTDutyChoiceLectureListView.as_view()),
    path('mgt_choice_lecture/<int:track_pk>/' , MGTChoiceLectureListView.as_view()),
    path('mgt_duty_lecture/<int:track_pk>/' , MGTDutyLectureListView.as_view()),
    path('eco_gicho_lecture/<int:track_pk>/' , ECOGichoLectureListView.as_view()),
    path('eco_choice_lecture/<int:track_pk>/' , ECOChoiceLectureListView.as_view()),
    path('eco_duty_lecture/<int:track_pk>/' , ECODutyLectureListView.as_view()),
    ###########################################################################33
    path('create_roadmap_details/', RoadmapDetailCreateView.as_view(), name='create_roadmap_details'),
    path('create_roadmap_detail_lecture/', RoadmapDetailLectureCreateView.as_view(), name='create_roadmap_detail_lecture'),
    path('completed_create_lecture/', CompletedLectureCreateView.as_view(), name='create_roadmap_detail_lecture'),


]