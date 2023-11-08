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
from rest_framework import status
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

import random
import json

from .models import *
from .serializers import UserSerializer

User = get_user_model()



def generate_verification_code():
    return str(random.randint(100000, 999999))


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
        student_number = request.POST.get('student_number')
        password = request.POST.get('password')
        
        user = authenticate(request, student_number=student_number, password=password)
        
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

class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class CustomTokenOBtainPairAPIView(TokenObtainPairView):
    pass