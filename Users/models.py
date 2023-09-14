from django.db import models
from Lectures.models import Major

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    student_number = models.IntegerField(unique=True)
    student_year = models.IntegerField()
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # major = models.ForeignKey(
    #     Major,
    #     on_delete=models.CASCADE,
    #     related_name='major_students'
    # )
    # submajor = models.ForeignKey(
    #     Major,
    #     on_delete=models.SET_NULL,
    #     related_name='submajor_students',
    #     null=True,
    #     blank=True
    # )
    completed_total = models.IntegerField(default=0)
    completed_common = models.IntegerField(default=0)
    completed_major = models.IntegerField(default=0)
    completed_submajor = models.IntegerField(default=0)
    completed_english = models.IntegerField(default=0)

    #학번에서 몇학번인지 추출해서 student_year에 따로 저장
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
        return f"{self.user}'s submajor-{self.major}"
