from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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


@csrf_exempt
def verify_email(request):
    if request.method == 'POST':
        email = request.data.get('email')
        verification_code = request.data.get('verification_code')
        try:
            user = User.objects.get(email = email, verification_code = verification_code)
            user.is_email_verified = True
            user.save()
            return JsonResponse({'message': 'Email verification successful. You can now complete the registration.'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'Invalid verification code'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        student_number = data.get('student_number')
        
        # 회원가입 시에 입력을 받나?
        # completed_total = data.get('completed_total')
        # completed_common = data.get('completed_common')
        # completed_major = data.get('completed_major')
        # completed_submajor1= data.get('completed_submajor1')
        # completed_submajor2= data.get('completed_submajor2')
        # completed_english= data.get('completed_english')
        try:
            validate_email(email)
            validate_email_domain(email)
        except ValidationError as e:
            return JsonResponse({'message': str(e)}, status=400)
        if email and password and name and student_number:
            verification_code = str(random.randint(100000, 999999))
            user = User.objects.create_user(email=email, password=password, name=name, student_number=student_number, verification_code=verification_code)
            send_mail(
                subject ='Email Verification',
                message = f'Your verification code is: {verification_code}',
                from_email = 'RTSsogangverify@gmail.com',
                recipient_list = [email],
                fail_silently = False,
            )
            return JsonResponse({'message': 'Verification code sent to your email. Please check your email and complete the registration.'})
    else:
        return JsonResponse({'message':'Invalid request method'}, status = 400)

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