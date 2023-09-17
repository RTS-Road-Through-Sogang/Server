from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields =  ('id', 'name','password','email', 'student_number','is_staff')
        extra_kwargs = {'password': {'write_only : True'}}
    
    def create(self, validated_data):
        user = MyUser(
            email = validated_data['email'],
            name = validated_data['name'],
            student_number = validated_data['student_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('student_number', )