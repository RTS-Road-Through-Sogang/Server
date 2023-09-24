from django.urls import path, include
from .views import *


urlpatterns = [
    path('<str:user_id>/', RoadMapList.as_view()),
    path('<str:user_id>/1/',RoadMapLectureList.as_view() ),
    path('<str:user_id>/2/',RoadmapFullView.as_view() )

]