from django.urls import path, include
from .views import *


urlpatterns = [
    path('',RoadmapFullView.as_view() ),
############################################################################################################################################################
    path('usermajortracks/',TrackByMajor.as_view()),
############################################################################################################################################################
    path('completed_lecture/',DoneLectures.as_view() )
]