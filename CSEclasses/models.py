from django.db import models
from Users.models import StudentYear
from Majors.models import Major, Category


# Create your models here.
class MajorTech(models.Model):
    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE,
        related_name='major_tech' #전공에 해당하는 테크. 재무, 마케팅 등등
    )
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title
    
class Track(models.Model):  #다전공, 심화전공...
    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE,
        related_name='major_track' #전공에 해당하는 트랙들. 
    )
    title = models.CharField(max_length=30) #(단일전공, 융합과정, 다전공  1전공, 다전공 타전공, 교직) (심화전공 = 단일전공/융합과정 , 일반전공 = 다전공 1전공, 다전공 타전공, 교직과정)
    student_year = models.ForeignKey(
        StudentYear,
        on_delete=models.CASCADE,
        related_name='studentyear_track' #학번에 해당하는 트랙
    )
    def __str__(self):
        return self.title
    
class MajorTrack(models.Model): #트랙당 전공이수학점이 달라서 해결하기 위함
    track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE,
        related_name='track_majortrack' #트랙에 해당하는 메이저트랙
    )
    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE,
        related_name='major_majortrack' #전공에 해당하는 메이저트랙
    )
    complete_point = models.IntegerField() #해당 전공 필수 총이수 학점
    gicho_point = models.IntegerField() #전공입문 학점
    duty_point = models.IntegerField() #전공필수 학점
    choice_point = models.IntegerField() #전공선택 학점
    # advance_point = models.IntegerField() #전공심화 학점

    def __str__(self):
        return f"{self.major} - {self.track}"

# class StudentYearCategory(models.Model):
#     student_year = models.ForeignKey(
#         StudentYear,
#         on_delete=models.CASCADE,
#         related_name='studentyear_sycategory', #studentyear에 해당하는 sycategory
#         null=True,
#         blank=True
#     )
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE,
#         related_name='category_sycategory', #category에 해당하는 sycategory
#         null=True,
#         blank=True
#     )
#     def __str__(self):
#         return f"{self.student_year} - {self.category}"

class Lecture(models.Model):
    title = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    point = models.IntegerField(choices=[(1,'1point'),(2,'2point'),(3,'3point')])
    eta = models.URLField(blank = True)
    semester_one = models.IntegerField(choices=[(1,'low'),(2,'mid'),(3,'high')])
    semester_two = models.IntegerField(choices=[(1,'low'),(2,'mid'),(3,'high')])
    teamplay = models.IntegerField(choices=[(1,'none'),(2,'little'),(3,'average'),(4,'much'),(5,'full')])
    former = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='latter', #후수강
        null=True,
        blank=True
    )
    grade_recommend = models.IntegerField(choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4')])
    season_open = models.BooleanField()
    category19 = models.ForeignKey(  #전선, 전필...
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
    # major = models.ForeignKey(
    #     Major,
    #     on_delete=models.CASCADE,
    #     related_name='major_lecture', #전공안에 렉처
    #     null=True,
    #     blank=True
    # )
    tech = models.ForeignKey(    #재무 마케팅...
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


