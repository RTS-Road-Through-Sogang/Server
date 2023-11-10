from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('verify_email/', sending_email, name='verify_email'),
    path('login/', CustomTokenOBtainPairAPIView.as_view(), name='token_obtain_pair'),
    path('logout/', logout_view, name='logout'),
    path('login/tokenrefresh/', TokenRefreshView.as_view(), name = "tokenrefresh"),
    path('student_number_duplicated/', student_number_duplicated, name = "student_number_duplicated"),
    path('email_duplicated/', email_duplicated, name = "email_duplicated"),
    path('password_forget/', password_forget, name="password_forget"),
    path('password_change/', password_change, name="password_change"),

]