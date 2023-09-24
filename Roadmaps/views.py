from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

class RoadMapList(generics.ListAPIView):
    queryset = Roadmap.objects.all()  
    serializer_class = RoadMapSerializer

    def get_queryset(self):
        
        user_id = self.kwargs['user_id']

        user = MyUser.objects.get(student_number=user_id)
        
        return Roadmap.objects.filter(student = user)

class RoadMapLectureList(generics.ListAPIView):
    queryset = RoadmapDetailLecture.objects.all()  
    serializer_class = RoadMapDetailLectureSerializer



class RoadMapDefault(generics.ListCreateAPIView):
    pass



# 새로 짠거 # 
##########################################
class RoadmapDetailView(generics.RetrieveAPIView):
    queryset = Roadmap.objects.all()  
    serializer_class = RoadMapSerializer

class RoadmapDetailListView(generics.ListAPIView):
    serializer_class = RoadMapDetailSerializer

    def get_queryset(self):
        roadmap_id = self.kwargs['roadmap_id']
        return RoadmapDetail.objects.filter(roadmap=roadmap_id)

class RoadmapDetailLectureListView(generics.ListAPIView):
    serializer_class = RoadMapDetailLectureSerializer

    def get_queryset(self):
        roadmap_detail_id = self.kwargs['roadmap_detail_id']
        return RoadmapDetailLecture.objects.filter(roadmap_detail=roadmap_detail_id)

class RoadmapFullView(generics.ListAPIView):
    queryset = Roadmap.objects.all()
    serializer_class = RoadMapSerializer

    
    
    def get(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        user = MyUser.objects.get(student_number=user_id)
        roadmaps = Roadmap.objects.filter(student=user)
        roadmap_data = {'roadmaps': []}
        for roadmap in roadmaps:
            roadmap_info = RoadMapSerializer(roadmap).data
            roadmap_details = RoadmapDetail.objects.filter(roadmap=roadmap)
            roadmap_info['roadmapdetaillecture'] = []

            for detail in roadmap_details:
                detail_data = RoadMapDetailSerializer(detail).data
                semester = detail_data['semester']  # Get the semester information
                detail_lectures = RoadmapDetailLecture.objects.filter(roadmap_detail=detail)
                detail_data['lectures'] = RoadMapDetailLectureSerializer(detail_lectures, many=True).data
                roadmap_info['roadmapdetaillecture'].append({
                    semester: detail_data['lectures']  # Add semester information
                })

            roadmap_data['roadmaps'].append(roadmap_info)

        return JsonResponse(roadmap_data['roadmaps'], safe=False)
