from rest_framework import serializers, fields
from .models import *
from MGTclasses.models import *
from Commonclasses.models import *
from CSEclasses.models import *
from ECOclasses.models import *
from ECOclasses.models import Lecture as EcoLecture
from MGTclasses.models import Lecture as MgtLecture
from Commonclasses.models import Lecture as CommonLecture
from CSEclasses.models import Lecture as CSELecture

from Users.models import *
from Roadmaps.models import *
from rest_framework import request
from Majors.models import *


class UserMajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMajor
        fields = ['major']
class CommonLectureDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonLecture
        fields ='__all__'

class ECOLectureDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcoLecture
        fields ='__all__'
class CSELectureDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSELecture
        fields ='__all__'
class MGTLectureDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MgtLecture
        fields ='__all__'
class CommonLectureDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonLecture
        fields ='__all__'


class LectureDetailSerializer(serializers.ModelSerializer):
    eco, cse, mgt, common = ECOLectureDetailSerializer(many=True, read_only = True), CSELectureDetailSerializer(many=True, read_only = True), MGTLectureDetailSerializer(many=True, read_only = True), CommonLectureDetailSerializer(many=True, read_only = True)
    model = ECOLecture
    fields = ['eco', 'cse', 'mgt', 'common']
    




"""class RoadMapDetailLectureSerializer(serializers.ModelSerializer):
    lectures_detail = LectureDetailSerializer(many=True, read_only=True)
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {key: value for key, value in data.items() if value is not None}
    class Meta:
        model = RoadmapDetailLecture
        fields = '__all__'"""



class RoadMapDetailLectureSerializer(serializers.ModelSerializer):

    common_name = CommonLectureDetailSerializer(source='commonlecture', read_only=True)
    eco_name = ECOLectureDetailSerializer(source='ecolecture', read_only=True)
    mgt_name = MGTLectureDetailSerializer(source='mgtlecture', read_only=True)
    cse_name = CSELectureDetailSerializer(source='cselecture', read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data['common_name'] is not None:
            data['common_name'] = data['common_name']['title']
        if data['eco_name'] is not None:
            data['eco_name'] = data['eco_name']['title']
        if data['mgt_name'] is not None:
            data['mgt_name'] = data['mgt_name']['title']
        if data['cse_name'] is not None:
            data['cse_name'] = data['cse_name']['title']

        return {key: value for key, value in data.items() if value is not None}

    class Meta:
        model = RoadmapDetailLecture
        fields = '__all__'

class RoadMapDetailSerializer(serializers.ModelSerializer):
    roadmapdetaillecture = RoadMapDetailLectureSerializer(many=True,read_only = True)
    class Meta:
        model = RoadmapDetail
        fields = ['semester', 'roadmapdetaillecture']


class RoadMapSerializer(serializers.ModelSerializer):
    roadmap_detail = RoadMapDetailSerializer(many=True, read_only=True)
    major = UserMajorSerializer(many=True, read_only=True)
    track = serializers.StringRelatedField()  
    student = serializers.StringRelatedField(source='student.student_number')
    
    class Meta:
        model = Roadmap
        fields = ['student', 'title', 'major', 'track', 'roadmap_detail']



