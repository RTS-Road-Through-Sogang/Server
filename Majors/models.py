from django.db import models

# Create your models here.
class Major(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title
    
class Category(models.Model):  #공필, 공선, 전입, 전필...
    title = models.CharField(max_length=10)
    detail = models.CharField(max_length=10, null=True, blank=True)
    duty_point = models.IntegerField(null=True, default=0) #각 세부당 필수 이수 학점
    def __str__(self):
        return f"{self.title} - {self.detail}"