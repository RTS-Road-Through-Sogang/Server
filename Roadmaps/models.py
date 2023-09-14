from django.db import models
from Users.models import User
from Lectures.models import Subject

class Roadmap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.name} - {self.name}"

class RoadmapDetail(models.Model):
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.roadmap.name} - {self.name}"

class SubjectInRoadmapDetail(models.Model):
    roadmap_detail = models.ForeignKey(RoadmapDetail, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.roadmap_detail.name} - {self.subject.name}"
