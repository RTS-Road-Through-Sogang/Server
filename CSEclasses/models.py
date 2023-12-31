from django.db import models
from Users.models import StudentYear, MyUser
from Majors.models import Major, Category


# Create your models here.
class MajorTech(models.Model):
    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE,
        related_name='CSE_tech' #전공에 해당하는 테크. 재무, 마케팅 등등
    )
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title
    
class Track(models.Model):  #다전공, 심화전공...
    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE,
        related_name='CSE_track' #전공에 해당하는 트랙들. 
    )
    title = models.CharField(max_length=30) #(단일전공, 융합과정, 다전공  1전공, 다전공 타전공, 교직) (심화전공 = 단일전공/융합과정 , 일반전공 = 다전공 1전공, 다전공 타전공, 교직과정)
    student_year = models.ForeignKey(
        StudentYear,
        on_delete=models.CASCADE,
        related_name='CSE_studentyear_track' #학번에 해당하는 트랙
    )
    def __str__(self):
        return f"{self.title} - {self.student_year} - {self.pk}"
    
class MajorTrack(models.Model): #트랙당 전공이수학점이 달라서 해결하기 위함
    track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE,
        related_name='track_CSEtrack' #트랙에 해당하는 메이저트랙
    )
    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE,
        related_name='major_CSEtrack' #전공에 해당하는 메이저트랙
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
    eta = models.URLField(blank=True)
    semester_one = models.IntegerField(blank=True)
    semester_two = models.IntegerField( blank=True)
    teamplay = models.IntegerField(choices=[(0,'none'),(1,'little'),(2,'average'),(3,'much'),(4,'full')], blank=True)
    former = models.CharField(max_length=60,null=True, blank=True)
    grade_recommend = models.CharField(max_length=10)
    season_open = models.BooleanField()
    label= models.CharField(max_length=30)

    category21 = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category21_CSE_lecture', #카테고리 안에 렉처
        null=True
    )
    category22 = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category22_CSE_lecture', #카테고리 안에 렉처
        null=True
    )
    category23 = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category23_CSE_lecture', #카테고리 안에 렉처
        null=True
    )
    category24 = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category24_CSE_lecture', #카테고리 안에 렉처
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
        related_name='majortech_CSE_lecture', #전공테크안에 렉처
        null=True,
        blank=True
    )
    teach = models.BooleanField() #교직 : 0이면 F 1이면 T
    advance = models.BooleanField() #심화 : 0이면 F 1이면 T

    def __str__(self):
        return f"{self.title}_{self.pk}"

class UserCSELecture(models.Model):
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='cselecture_User',
        null=True,
        blank=True
    )
    cselecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
        related_name='cselecture_completed',
        null=True,
        blank=True
    )
    def __str__(self):
        return f"{self.user} has completed {self.cselecture.title}"
