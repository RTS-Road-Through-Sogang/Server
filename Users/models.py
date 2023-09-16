from django.db import models
from Majors.models import Major

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=10, unique=True)
    student_year = models.IntegerField(null=True, blank=True, default=0)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    completed_total = models.IntegerField(default=0)
    completed_common = models.IntegerField(default=0)
    completed_major = models.IntegerField(default=0)
    completed_submajor1 = models.IntegerField(default=0, null=True)
    completed_submajor2 = models.IntegerField(default=0, null=True)
    completed_english = models.IntegerField(default=0)

    # 학번에서 몇학번인지 User에서 추출해서 student_year에 따로 저장
    def save(self, *args, **kwargs):
        if self.student_number and len(self.student_number) >= 4:
            year = self.student_number[2:4]
            try:
                student_year = int(year)
            except ValueError:
                student_year = None
        else:
            student_year = None
        self.student_year = student_year
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class StudentYear(models.Model):

    student_year = models.IntegerField()

    # #학번에서 몇학번인지 User에서 추출해서 student_year에 따로 저장
    # def save(self, *args, **kwargs):
    #     if User.student_number and len(User.student_number) >= 4:
    #         year = User.student_number[2:4]
    #         try:
    #             student_year = int(year)
    #         except ValueError:
    #             student_year = None
    #     else:
    #         student_year = None
    #     self.student_year = student_year
    #     super(User, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.student_year)
    
class UserMajor(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_submajor' #유저의 부전공
    )
    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE,
        related_name='major_submajor' #전공중 부전공으로 선택된것
    )
    prime = models.BooleanField()
    completed = models.IntegerField(default=0) #해당전공 이수 학점

    def __str__(self):
        if self.prime==0:
            return f"{self.user}'s submajor-{self.major}"
        else:
            return f"{self.user}'s primemajor-{self.major}"
