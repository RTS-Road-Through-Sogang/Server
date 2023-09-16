from django.db import models
from Users.models import User
from CSEclasses.models import Track, Lecture

# Create your models here.
class Roadmap(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student_roadmap'
    )
    title = models.CharField(max_length = 10) #1안 2안
    track = models.ForeignKey(  #다전공, 심화전공...
        Track,
        on_delete=models.CASCADE,
        related_name='track_roadmap'
    )
    
    def __str__(self):
        return f"{self.student}_{self.title}"
    
class RoadmapDetail(models.Model):
    semester = models.CharField(max_length=20) #1-1 1-S
    roadmap = models.ForeignKey(
        Roadmap,
        on_delete=models.CASCADE,
        related_name='roadmap_detail',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.roadmap.student}_{self.roadmap.title}_{self.semester}"
    
class RoadmapDetailLecture(models.Model):
    roadmap_detail = models.ForeignKey(
        RoadmapDetail,
        on_delete=models.CASCADE,
        related_name='roadmap_detail',
        null=True,
        blank=True
    )
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
        related_name='lecture_roadmap_detail', #렉처를 담은 로드맵 디테일
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.roadmap_detail.roadmap.student}_{self.roadmap_detail.roadmap.title}_{self.roadmap_detail.semester}_{self.lecture}"
