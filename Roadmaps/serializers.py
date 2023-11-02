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
from CSEclasses.models import MajorTech as CSETech
from ECOclasses.models import MajorTech as ECOTech
from MGTclasses.models import MajorTech as MGTTech

from Users.models import *
from Roadmaps.models import *
from rest_framework import request
from Majors.models import *


class UserMajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMajor
        fields = ['major']


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

# 그냥 생성을 위해서 필요함
class RoadMapSerializers(serializers.ModelSerializer):
    student = serializers.StringRelatedField(source='student.student_number')

    class Meta:
        model = Roadmap
        fields =["student"]
        

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

    def get_major_tracks(self, obj): #obj가 user_a
        student_year = obj.student_year
        major = obj.major
        all_tracks = []

        if major.title == "컴퓨터공학":
            cse_tracks = CSETrack.objects.filter(major=major, student_year__student_year=student_year).exclude(title="다전공 타전공")
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
                    {"major": "컴퓨터공학"},
                    {"major": "경제"}
                ]
            }
            mgt_track_info.update(second_major_info)
            
            all_tracks.append(mgt_track_info)
        elif major.title == "경제":
            eco_tracks = ECOTrack.objects.filter(major=major, student_year__student_year=student_year).exclude(title="다전공 타전공")
            eco_serialized = TrackSerializer(eco_tracks, many=True).data
            all_tracks.append({'ECO_tracks': eco_serialized})
            second_major_info = {
                "second_major": [
                    {"major": "컴퓨터공학"},
                    {"major": "경영"}
                ]
            }
        all_tracks.append(second_major_info)
        return all_tracks

class CommonLectureListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonLecture
        fields = '__all__'  # 필요한 필드를 지정하거나 '__all__'을 사용하여 모든 필드를 직렬화할 수 있습니다.
############################################################################################################################################################


class alllectures(serializers.Serializer):
    common_name = CommonLectureDetailSerializer(many=True,read_only=True)
    eco_name = ECOLectureDetailSerializer(many=True,read_only=True)
    mgt_name = MGTLectureDetailSerializer(many=True,read_only=True)
    cse_name = CSELectureDetailSerializer(many=True,read_only=True)
########################################################################################
class RoadmapDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoadmapDetail
        fields = "__all__"
    
class RoadmapSerializers(serializers.ModelSerializer):
    class Meta:
        model = Roadmap
        fields = "__all__"

class RoadmapsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Roadmap
        fields = ['title']
    
########################################################################################33333
# roadmap (맨처음거 만들고난 추후)만들기 새로만들기 누르면 자동으로 roadmap_id가 흘러들어간다
class RoadmapDetailCreateSerializer(serializers.Serializer):
    roadmap_id = serializers.IntegerField()
    # 여기서 roadmap_id를 받는걸로 되어있지만 추후에 프론트랑 이야기해서 변경해야함
    def create(self, validated_data):
        roadmap_id = validated_data.get('roadmap_id') 
        roadmap = Roadmap.objects.get(pk=roadmap_id) # Get roadmap_id
        titles = ['1-1', '1-하계','1-2','1-동계', '2-1', '2-하계', '2-2','2-동계', '3-1','3-하계', '3-2','3-동계' , '4-1','4-하계', '4-2','4-동계']

        for title in titles:
            RoadmapDetail.objects.create(
                semester=title,
                roadmap =roadmap  # Use roadmap_id here
            )

        return roadmap_id
    #########################################################################################3
class RoadmapDetailLectureCreateSerializer(serializers.ModelSerializer):
    roadmap_detail_id = serializers.IntegerField()
    lecture_type = serializers.CharField()
    lecture_id = serializers.IntegerField()

    class Meta:
        model = RoadmapDetailLecture
        fields = '__all__'

    # user 어쩌구도 저장되도록 만들어야 함
    def create(self, validated_data):
        roadmap_detail_id = validated_data.get('roadmap_detail_id')
        lecture_type = validated_data.get('lecture_type')
        lecture_id = validated_data.get('lecture_id')
        
        try:
            if lecture_type == 'commonlecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                commonlecture = CommonLecture.objects.get(pk=lecture_id)
                
                return RoadmapDetailLecture.objects.create(
                    roadmap_detail=roadmap_detail,
                    commonlecture=commonlecture
                )

            elif lecture_type == 'cselecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                cselecture = CSELecture.objects.get(pk=lecture_id)

                return RoadmapDetailLecture.objects.create(
                    roadmap_detail=roadmap_detail,
                    cselecture=cselecture
                )

            elif lecture_type == 'ecolecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                ecolecture = ECOLecture.objects.get(pk=lecture_id)

                return RoadmapDetailLecture.objects.create(
                    roadmap_detail=roadmap_detail,
                    ecolecture=ecolecture
                )

            elif lecture_type == 'mgtlecture':
                roadmap_detail = RoadmapDetail.objects.get(pk=roadmap_detail_id)
                commonlecture = CommonLecture.objects.get(pk=lecture_id)  

                if roadmap_detail and commonlecture:
                    return RoadmapDetailLecture.objects.create(
                        roadmap_detail=roadmap_detail,
                        commonlecture=commonlecture
                    )
                else:
                    raise serializers.ValidationError("Invalid roadmap_detail or commonlecture")


            else:
                raise serializers.ValidationError("Invalid lecture type")
        except RoadmapDetail.DoesNotExist as e:
            raise serializers.ValidationError(f"RoadmapDetail with id {roadmap_detail_id} does not exist.")
        except CommonLecture.DoesNotExist as e:
            raise serializers.ValidationError(f"CommonLecture with id {lecture_id} does not exist.")
        except CSELecture.DoesNotExist as e:
            raise serializers.ValidationError(f"CSELecture with id {lecture_id} does not exist.")
        except ECOLecture.DoesNotExist as e:
            raise serializers.ValidationError(f"ECOLecture with id {lecture_id} does not exist.")
        except MGTLecture.DoesNotExist as e:
            raise serializers.ValidationError(f"MGTLecture with id {lecture_id} does not exist.")

###################################################################################################################
#처음 등록시 user lecture에 넣어주는 역할
class CompletedLectureCreateSerializer(serializers.ModelSerializer):
    lecture_type = serializers.CharField()
    lecture_id = serializers.IntegerField()

    class Meta:
        model = RoadmapDetailLecture
        fields = '__all__'

    # user 어쩌구도 저장되도록 만들어야 함
    def create(self, request, validated_data):
        user_id = self.request.user
        lecture_type = validated_data.get('lecture_type')
        lecture_id = validated_data.get('lecture_id')
        
        try:
            if lecture_type == 'commonlecture':
                
                commonlecture = CommonLecture.objects.get(pk=lecture_id)
                
                return UserCommonLecture.objects.create(
                    user=user_id,
                    commonlecture=commonlecture
                )

            elif lecture_type == 'cselecture':
                cselecture = CSELecture.objects.get(pk=lecture_id)

                return UserCSELecture.objects.create(
                    user=user_id,
                    cselecture=cselecture
                )

            elif lecture_type == 'ecolecture':
                ecolecture = ECOLecture.objects.get(pk=lecture_id)

                return UserECOLecture.objects.create(
                    user=user_id,
                    ecolecture=ecolecture
                )

            elif lecture_type == 'mgtlecture':
                commonlecture = CommonLecture.objects.get(pk=lecture_id)  

                if commonlecture:
                    return UserMGTLecture.objects.create(
                        user=user_id,
                        commonlecture=commonlecture
                    )
                else:
                    raise serializers.ValidationError("Invalid roadmap_detail or commonlecture")


            else:
                raise serializers.ValidationError("Invalid lecture type")
        except CommonLecture.DoesNotExist as e:
            raise serializers.ValidationError(f"CommonLecture with id {lecture_id} does not exist.")
        except CSELecture.DoesNotExist as e:
            raise serializers.ValidationError(f"CSELecture with id {lecture_id} does not exist.")
        except ECOLecture.DoesNotExist as e:
            raise serializers.ValidationError(f"ECOLecture with id {lecture_id} does not exist.")
        except MGTLecture.DoesNotExist as e:
            raise serializers.ValidationError(f"MGTLecture with id {lecture_id} does not exist.")
        ########################################################################################
        # 학점 계산 한거 보여주기

class RoadmapDetailCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoadmapDetail
        fields = ['roadmap']