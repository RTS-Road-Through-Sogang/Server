from django.db import models



# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class StudentNumber(models.Model):
    number = models.IntegerField(default=25)

    def __str__(self):
        return str(self.number)

class User(models.Model):
    name = models.CharField(max_length=50)
    student_number = models.ForeignKey(StudentNumber, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    school_email = models.EmailField()
    primary_major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name='primary_major_users')
    secondary_major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name='secondary_major_users', null=True, blank=True)

    def __str__(self):
        return self.name
