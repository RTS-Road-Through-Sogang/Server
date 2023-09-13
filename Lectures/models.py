from django.db import models
from Roadmaps.models import *
from Users.models import *

# Create your models here.

class Major(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=10)
    detail = models.CharField(max_length=30)

class MajorTech(models.Model):
    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE,
        related_name='major_tech' #전공에 해당하는 테크
    )
    title = models.CharField(max_length=30)

class Track(models.Model):
    title = models.CharField(max_length=30)


# class Track_Lecture(models.Model):
    

class Lecture(models.Model):
    title = models.CharField()
    code = models.CharField()
    point = models.IntegerField(choices=[(1,'1'),(2,'2'),(3,'3')])
    eta = models.URLField(blank = True)
    semester_one = models.IntegerField(choices=[(1,'1'),(2,'2'),(3,'3')])
    semester_two = models.IntegerField(choices=[(1,'1'),(2,'2'),(3,'3')])
    teamplay = models.IntegerField(choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')])
    former = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='latter', #후수강
        null=True,
        blank=True
    )
    grade_recommend = models.IntegerField(choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4')])
    category19 = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category19_lecture', #카테고리 안에 렉처
        null=True
    )
    category20 = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category20_lecture', #카테고리 안에 렉처
        null=True
    )
    category21 = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category21_lecture', #카테고리 안에 렉처
        null=True
    )
    category22 = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category22_lecture', #카테고리 안에 렉처
        null=True
    )
    category23 = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category23_lecture', #카테고리 안에 렉처
        null=True
    )
    category24 = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category24_lecture', #카테고리 안에 렉처
        null=True
    )
    # category = models.ForeignKey(
    #     Category,
    #     on_delete=models.CASCADE,
    #     related_name='category_lecture' #카테고리 안에 렉처
    # )
    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE,
        related_name='major_lecture', #전공안에 렉처
        null=True,
        blank=True
    )
    season_open = models.BooleanField()
    tech = models.ForeignKey(
        MajorTech,
        on_delete=models.CASCADE,
        related_name='majortech_lecture', #전공테크안에 렉처
        null=True,
        blank=True
    )
    teach = models.BooleanField() #교직 : 0이면 F 1이면 T
    advance = models.BooleanField() #심화 : 0이면 F 1이면 T

    def __str__(self):
        return self.title


