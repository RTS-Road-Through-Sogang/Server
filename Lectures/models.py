from django.db import models
from Users.models import *
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    student_numbers = models.OneToOneField(StudentNumber, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tech(models.Model):
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.major.name} - {self.name}"



class CategoryDetail(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=10)
    credits = models.IntegerField()
    eta_url = models.URLField()
    semester_1 = models.BooleanField()
    semester_2 = models.BooleanField()
    team_project = models.BooleanField()
    prerequisite = models.ManyToManyField('self', blank=True)
    recommended_grade = models.CharField(max_length=10)
    category_detail = models.OneToOneField(CategoryDetail, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    tech = models.ManyToManyField(Tech, blank=True, through='TechInSubject')
    is_education = models.BooleanField()
    is_advanced = models.BooleanField()

    def __str__(self):
        return self.name

class Route(models.Model):
    name = models.CharField(max_length=50)
    student_number = models.ForeignKey(StudentNumber, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, through='SubjectInRoute')
    def __str__(self):
        return f"{self.student_number.number} - {self.major.name} - {self.name}"
    
class TechInSubject(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE)
    student_number = models.ForeignKey(StudentNumber, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject.name} - {self.tech.name} - {self.student_number.number}"
    


class SubjectInRoute(models.Model):
    root = models.ForeignKey(Route, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.root.name} - {self.subject.name}"
