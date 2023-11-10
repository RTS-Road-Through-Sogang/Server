from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from Majors import *
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import status
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

import random
import json
import string
from .models import *
from .serializers import UserSerializer

User = get_user_model()



def generate_verification_code():
    return str(random.randint(100000, 999999))
def new_password():
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(6))
    return random_string

"""@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        student_number = data.get('student_number')
        prime_major = data.get('major')


        try:
            
            validate_email(email)  # 이메일 형식 검증
            validate_email_domain(email)  # 도메인 검증
        except ValidationError as e:
            return JsonResponse({'message': str(e)}, status=400)

        if email and password and name and student_number:
            # 인증 코드 생성 및 저장
            verification_code = generate_verification_code()
            majors = Major.objects.get(title=prime_major)
            
            user = User.objects.create_user(email=email, password=password, name=name, student_number=student_number, verification_code=verification_code,major = majors )
            user_major = UserMajor.create_usermajor(user=user, major=majors, prime=True, completed=0)
            # 인증 메일 전송
            send_mail(
                'Email Verification',
                f'Your verification code is: {verification_code}',
                'rtssogang@gmail.com',
                [email],
                fail_silently=False,
            )

            return JsonResponse({'message': 'Verification code sent to your email. Please check your email and complete the registration.'})
        return JsonResponse({'message': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)


@csrf_exempt
def verify_email(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        verification_code = data.get('verification_code')
        try:
            user = User.objects.get(email = email, verification_code = verification_code)
            user.is_email_verified = True
            user.save()
            return JsonResponse({'message': 'Email verification successful. You can now complete the registration.'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'Invalid verification code'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
"""
        
@csrf_exempt
def sending_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        """try:
            
            validate_email(email)  # 이메일 형식 검증
            validate_email_domain(email)  # 도메인 검증
        except ValidationError as e:
            return JsonResponse({'message': str(e)}, status=400)"""
        verification_code = generate_verification_code()
        # 인증 메일 전송
        send_mail(
                'Email Verification',
                f'Your verification code is: {verification_code}',
                'rtssogang@gmail.com',
                [email],
                fail_silently=False,
            )
        return JsonResponse({'message': f'이 숫자 6자리 검사해주세요 {verification_code} '})
    else:
        return JsonResponse({'message': 'post로 처리되어야함'}, status=400)    
        
@csrf_exempt
def email_duplicated(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        user = MyUser.objects.all()
        for u in user:
            if email == u.email:
                return JsonResponse({"message": "the email is duplicated"}, status=400)
        return JsonResponse({"message": "OK good"})
    else:
        return JsonResponse({'message': 'only POST'}, status=400)

@csrf_exempt
def student_number_duplicated(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student_number = data.get('student_number')
        user = MyUser.objects.all()
        for u in user:
            if student_number == u.student_number:
                return JsonResponse({"message": "the student_number is duplicated"}, status=400)
        return JsonResponse({"message": "OK good"})
    else:
        return JsonResponse({'message': 'only POST'}, status=400)
        
@csrf_exempt
def password_forget(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student_number = data.get('student_number')
        email = data.get('email')
        print(student_number)
        print(email)
        try:
            user = MyUser.objects.get(email=email, student_number=student_number)
        except MyUser.DoesNotExist:
            return JsonResponse({"message": "이메일과 학번이 일치하지 않습니다"}, status=400)
        
        
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(6))
        new_password = random_string
        print(new_password)
        
        
        user.set_password(new_password)
        user.save()
        
       
        send_mail(
            '새로운 비밀번호',
            f'새로운 비밀번호는: {new_password} 입니다.',
            'rtssogang@gmail.com',
            [email],
            fail_silently=False,
        )
        
        return JsonResponse({"message": "비밀번호가 변경되었습니다"})
    else:
        return JsonResponse({'message': 'POST 요청만 허용됩니다'}, status=400)

@csrf_exempt
def password_change(request):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        new_password = data.get('new_password')     
        user = request.user 
        """if original_password != checking_user.password:
            return JsonResponse({"message": "기존 비밀번호가 올바르지 않습니다"})"""
        
        user.set_password(new_password)
        user.save()
        return JsonResponse({"message": "비밀번호가 변경되었습니다"})  
        
            


@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        student_number = data.get('student_number')
        prime_major = data.get('major')

        if email and password and name and student_number:
            # 인증 코드 생성 및 저장
            majors = Major.objects.get(title=prime_major)
            
            user = User.objects.create_user(email=email, password=password, name=name, student_number=student_number,major = majors )
            user_major = UserMajor.create_usermajor(user=user, major=majors, prime=True, completed=0)
            
            return JsonResponse({'message': 'signup completed'})
        return JsonResponse({'message': 'email password name student name error'}, status=400)
    else:
        return JsonResponse({'message': 'only POST'}, status=400)
    
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login Success!'})
        else:
            messages.error(request, '이메일이나 비밀번호가 잘못되었습니다.')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, '로그아웃되었습니다.')
    return JsonResponse({"message" : "Logout Success!"},status=status.HTTP_201_CREATED)
###
class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class CustomTokenOBtainPairAPIView(TokenObtainPairView):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        student_number = data.get('student_number')
        password = data.get('password')
        user = authenticate(request, student_number=student_number, password=password)
        print(user)
        if user is not None:
            login(request, user)
            tokens = self.get_tokens(user)

            return JsonResponse({
                'access': str(tokens['access']),
                'refresh': str(tokens['refresh']),
            })
        else:
            return JsonResponse({'message': 'Login failed'}, status=401)
    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }