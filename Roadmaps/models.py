from django.db import models
from django.conf import settings

from Commonclasses.models import Lecture as CommonLecture
from CSEclasses.models import Track as CSETrack, Lecture as CSELecture
from MGTclasses.models import Track as MGTTrack, Lecture as MGTLecture
from ECOclasses.models import Track as ECOTrack, Lecture as ECOLecture

# Create your models here.
class Roadmap(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_roadmap'
    )
    title = models.CharField(max_length = 20) #1안 2안
    
    
    def __str__(self):
        return f"{self.student}_{self.title}-{self.pk}"
    
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
        return f"{self.roadmap.student}_{self.roadmap.title}_{self.semester}_{self.pk}"
    
class RoadmapDetailLecture(models.Model):
    completed = models.BooleanField(null=True, default = False)
    roadmap_detail = models.ForeignKey(
        RoadmapDetail,
        on_delete=models.CASCADE,
        related_name='roadmap_detail',
        null=True,
        blank=True
    )
    commonlecture = models.ForeignKey(
        CommonLecture,
        on_delete=models.CASCADE,
        related_name='cselecture_roadmap_detail', #렉처를 담은 로드맵 디테일
        null=True,
        blank=True
    )
    cselecture = models.ForeignKey(
        CSELecture,
        on_delete=models.CASCADE,
        related_name='cselecture_roadmap_detail', #렉처를 담은 로드맵 디테일
        null=True,
        blank=True
    )
    mgtlecture = models.ForeignKey(
        MGTLecture,
        on_delete=models.CASCADE,
        related_name='mgtlecture_roadmap_detail', #렉처를 담은 로드맵 디테일
        null=True,
        blank=True
    )
    ecolecture = models.ForeignKey(
        ECOLecture,
        on_delete=models.CASCADE,
        related_name='ecolecture_roadmap_detail', #렉처를 담은 로드맵 디테일
        null=True,
        blank=True
    )

    def __str__(self):
        if self.commonlecture:
            return f"{self.roadmap_detail.roadmap.student}_{self.roadmap_detail.roadmap.title}_{self.roadmap_detail.semester}_{self.commonlecture.title}"
        elif self.cselecture:
            return f"{self.roadmap_detail.roadmap.student}_{self.roadmap_detail.roadmap.title}_{self.roadmap_detail.semester}_{self.cselecture.title}"
        elif self.mgtlecture:
            return f"{self.roadmap_detail.roadmap.student}_{self.roadmap_detail.roadmap.title}_{self.roadmap_detail.semester}_{self.mgtlecture.title}"
        elif self.ecolecture:
            return f"{self.roadmap_detail.roadmap.student}_{self.roadmap_detail.roadmap.title}_{self.roadmap_detail.semester}_{self.ecolecture.title}"
