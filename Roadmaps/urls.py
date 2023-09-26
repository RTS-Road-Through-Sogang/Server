from django.urls import path, include
from .views import *


urlpatterns = [
    path('<str:user_id>/',RoadmapFullView.as_view() ),
    path('usermajortracks/<int:pk>/',TrackByMajor.as_view()),
]