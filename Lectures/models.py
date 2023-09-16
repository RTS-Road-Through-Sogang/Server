from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

class CategoryDetail(models.Model):
    name = models.CharField(max_length=100)

class CategoryDetailMembership(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    detail = models.ForeignKey(CategoryDetail, on_delete=models.CASCADE)

class Track(models.Model):
    name = models.CharField(max_length=100)

class TrackMembership(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

class StudentID(models.Model):
    student_id = models.CharField(max_length=10, unique=True)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

class SubjectEnrollment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student_id = models.ForeignKey(StudentID, on_delete=models.CASCADE)


class Major(models.Model):
    name = models.CharField(max_length=100)

class Track(models.Model):
    name = models.CharField(max_length=100)


class User(models.Model):
    username = models.CharField(max_length=50)
    student_id = models.OneToOneField('StudentID', on_delete=models.CASCADE, null=True, blank=True)

class UserMajor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)



class MajorTech(models.Model):
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)



class TrackMajor(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)

class TrackMembership(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
