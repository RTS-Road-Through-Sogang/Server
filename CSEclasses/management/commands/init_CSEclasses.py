
from django.core.management.base import BaseCommand
from Majors.models import *
from CSEclasses.models import *


class Command(BaseCommand):
    tracks = [
        {
            'major': '컴퓨터공학',
            'title':'단일전공',
            'student_year': 23
        },
        {
            'major': '컴퓨터공학',
            'title':'융합과정',
            'student_year': 23
        },
        {
            'major': '컴퓨터공학',
            'title':'다전공 1전공',
            'student_year': 23
        },
        {
            'major': '컴퓨터공학',
            'title':'다전공 타전공',
            'student_year': 23
        },
        {
            'major': '컴퓨터공학',
            'title':'교직과정',
            'student_year': 23
        },
        {
            'major': '컴퓨터공학',
            'title':'단일전공',
            'student_year': 22
        },
        {
            'major': '컴퓨터공학',
            'title':'융합과정',
            'student_year': 22
        },
        {
            'major': '컴퓨터공학',
            'title':'다전공 1전공',
            'student_year': 22
        },
        {
            'major': '컴퓨터공학',
            'title':'다전공 타전공',
            'student_year': 22
        },
        {
            'major': '컴퓨터공학',
            'title':'교직과정',
            'student_year': 22
        },
        {
            'major': '컴퓨터공학',
            'title':'단일전공',
            'student_year': 21
        },
        {
            'major': '컴퓨터공학',
            'title':'융합과정',
            'student_year': 21
        },
        {
            'major': '컴퓨터공학',
            'title':'다전공 1전공',
            'student_year': 21
        },
        {
            'major': '컴퓨터공학',
            'title':'다전공 타전공',
            'student_year': 21
        },
        {
            'major': '컴퓨터공학',
            'title':'교직과정',
            'student_year': 21
        },
        
    ]
    
    MajorTrack =[
        {
            # 단일전공 21학번 쭉
            'track': 1,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 16 ,
            'duty_point' : 36 ,
            'choice_point' : 36
        },
        {
            # 융합과정
            'track': 2,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 16 ,
            'duty_point' : 36 ,
            'choice_point' : 24
        },
        {
            # 다전공 1전공
            'track': 3,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 6 ,
            'duty_point' : 36 ,
            'choice_point' : 24
        },
        {
            # 다전공 타전공
            'track': 4,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 3 ,
            'duty_point' : 6 ,
            'choice_point' : 33
        },
        {
            # 교직전공
            'track': 5,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 13 ,
            'duty_point' : 45 ,
            'choice_point' : 15
        },
        {
            # 단일전공 21학번 쭉
            'track': 6,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 16 ,
            'duty_point' : 36 ,
            'choice_point' : 36
        },
        {
            # 융합과정
            'track': 7,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 16 ,
            'duty_point' : 36 ,
            'choice_point' : 24
        },
        {
            # 다전공 1전공
            'track': 8,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 6 ,
            'duty_point' : 36 ,
            'choice_point' : 24
        },
        {
            # 다전공 타전공
            'track': 9,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 3 ,
            'duty_point' : 6 ,
            'choice_point' : 33
        },
        {
            # 교직전공
            'track': 10,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 13 ,
            'duty_point' : 45 ,
            'choice_point' : 15
        },
        {
            # 단일전공 21학번 쭉
            'track': 11,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 16 ,
            'duty_point' : 36 ,
            'choice_point' : 36
        },
        {
            # 융합과정
            'track': 12,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 16 ,
            'duty_point' : 36 ,
            'choice_point' : 24
        },
        {
            # 다전공 1전공
            'track': 13,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 6 ,
            'duty_point' : 36 ,
            'choice_point' : 24
        },
        {
            # 다전공 타전공
            'track': 14,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 3 ,
            'duty_point' : 6 ,
            'choice_point' : 33
        },
        {
            # 교직전공
            'track': 15,
            'major': '컴퓨터공학',
            'complete_point' : 130,
            'gicho_point' : 13 ,
            'duty_point' : 45 ,
            'choice_point' : 15
        }
    ]
    
    
    
    def handle(self, *args, **options):
        for track in self.tracks:
            Track.objects.get_or_create(
                major = Major.objects.get(title = track['major']),
                title = track['title'],
                student_year = StudentYear.objects.get(student_year=track['student_year'])
            )
        for majortrack in self.MajorTrack:
            MajorTrack.objects.get_or_create(
                track = Track.objects.get(pk=majortrack['track']),
                major =  Major.objects.get(title="컴퓨터공학"),
                complete_point = majortrack['complete_point'],
                gicho_point = majortrack['gicho_point'],
                duty_point = majortrack['duty_point'],
                choice_point = majortrack['choice_point']
            
            )

        self.stdout.write(self.style.SUCCESS('Tracks initialized'))
        return 0
            
        