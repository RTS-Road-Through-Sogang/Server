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
from CSEclasses.models import Track as CSETrack 
from ECOclasses.models import Track as ECOTrack
from MGTclasses.models import Track as MGTTrack

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

############################################################################################################################################################
# Track 반환을 위한 Serializers
class StudentYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentYear
        fields = ('student_year',)

class TrackSerializer(serializers.Serializer):
    title = serializers.CharField()
    major = serializers.PrimaryKeyRelatedField(read_only=True)
    student_year = StudentYearSerializer()
    class Meta:
        model = Track
        fields = ('title', 'major', 'student_year')

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ('title',)


class UserMajorTrackSerializer(serializers.ModelSerializer):
    major = MajorSerializer()
    major_tracks = serializers.SerializerMethodField()
    # major = UserMajorSerializer(many=True, read_only=True)
    class Meta:
        model = MyUser
        fields = ('name', 'major', 'major_tracks')
    
    # def get_major(self, obj):
    #     return obj.major.title

    def get_major_tracks(self, obj):
        student_year = obj.student_year
        major = obj.major
        all_tracks = []

        if major.title == "컴퓨터공학":
            cse_tracks = CSETrack.objects.filter(major=major, student_year=student_year).exclude(title="다전공 타전공")
            cse_serialized = TrackSerializer(cse_tracks, many=True).data
            all_tracks.append({'CSE_tracks': cse_serialized})
            second_major_info = {
                "second_major": [
                    {"major1": "경영"},
                    {"major2": "경제"}
                ]
            }
        elif major.title == "경영":
            mgt_tracks = MGTTrack.objects.filter(major=major, student_year__student_year=student_year).exclude(title="다전공 타전공")
            mgt_serialized = TrackSerializer(mgt_tracks, many=True).data
            mgt_track_info = {'MGT_tracks': mgt_serialized}
            
            # Add second major information here
            second_major_info = {
                "second_major": [
                    {"major": "컴퓨터공헉"},
                    {"major": "경제"}
                ]
            }
            mgt_track_info.update(second_major_info)
            
            all_tracks.append(mgt_track_info)
        elif major.title == "경제":
            eco_tracks = ECOTrack.objects.filter(major=major, student_year=student_year).exclude(title="다전공 타전공")
            eco_serialized = TrackSerializer(eco_tracks, many=True).data
            all_tracks.append({'ECO_tracks': eco_serialized})
            second_major_info = {
                "second_major": [
                    {"major": "컴퓨터공학"},
                    {"major": "경제"}
                ]
            }
        return all_tracks
############################################################################################################################################################


class alllectures(serializers.ModelSerializer):
    common_name = CommonLectureDetailSerializer(source='commonlecture', read_only=True)
    eco_name = ECOLectureDetailSerializer(source='ecolecture', read_only=True)
    mgt_name = MGTLectureDetailSerializer(source='mgtlecture', read_only=True)
    cse_name = CSELectureDetailSerializer(source='cselecture', read_only=True)
    class Meta:
        model = CommonLecture
        fields = "__all__"