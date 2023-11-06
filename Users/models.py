from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from Majors.models import Major

def validate_email_domain(value):
    valid_domains = ['sogang.ac.kr']
    email = value.split('@')
    if len(email) == 2 and email[1] in valid_domains:
        return True
    raise ValidationError("서강대학교 도메인 주소를 통한 이메일 인증만 가능합니다.")

class MyUserManager(BaseUserManager):
    def create_user(self, email, student_number, password=None, **extra_fields):
        if not email:
            raise ValueError("올바른 이메일 주소를 입력하세요.")
        if not student_number:
            raise ValueError("올바른 학번을 입력하세요.")
        
        user = self.model(
            email = self.normalize_email(email),
            student_number = student_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, student_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, student_number, password, **extra_fields)

class MyUser(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=10, unique=True)
    student_year = models.IntegerField(null=True, blank=True, default=0)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    completed_english = models.IntegerField(default=0)
    
    is_email_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name= "prime_major", null=True)
    objects = MyUserManager()
    
    USERNAME_FIELD = 'student_number'
    REQUIRED_FIELDS =['name', 'email']

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
        super(MyUser, self).save(*args, **kwargs)

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
        MyUser,
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
    def create_usermajor(user, major, prime, completed):
        user_major = UserMajor(user=user, major=major, prime=prime, completed=completed)
        user_major.save()
        return user_major
            
class CompletedEng(models.Model):
    completedeng = models.IntegerField()
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='User_completedeng', #유저가 완료한 영강학점 찾을때
        null=True,
        blank=True
    )
    def __str__(self):
        return f"{self.user} has completed {self.completedeng} point of eng"