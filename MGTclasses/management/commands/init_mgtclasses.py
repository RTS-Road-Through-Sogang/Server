from django.core.management.base import BaseCommand
from MGTclasses.models import *
from Majors.models import *
class Command(BaseCommand):
    
    help = 'Initialize , MGT'
    MajorTech = [  
        {

            'title' : '회계'
            
        }, 
        {
            'title' : '재무'
            
        }, 
        {
            'title' : '보험'
            
        }, 
        {
            'title' : '인사조직'
            
        }, 
        {
            'title' : '전략'
            
        }, 
        {
            'title' : '마케팅'
            
        },
        {
            'title' : '국제경영'
            
        }, 
        {
            'title' : 'BA'
            
        },
        {
            'title' : 'LSOM'
            
        },
        {
            'title' : 'MIS'
            
        },
        {
            'title' : '기타'
            
        }, 
        
    ]
    
    Track = [
        {
            'major': 1,
            'title': '다전공 1전공',
            'student_year': 1
        },
        {
            'major': 1,
            'title': '다전공 1전공',
            'student_year': 2
        },
        {
            'major': 1,
            'title': '다전공 1전공',
            'student_year': 3
        },
        {
            'major': 1,
            'title': '다전공 타전공',
            'student_year': 1
        },
        {
            'major': 1,
            'title': '다전공 타전공',
            'student_year': 2
        },
        {
            'major': 1,
            'title': '다전공 타전공',
            'student_year': 3
        },
        {
            'major': 1,
            'title': '단일전공',
            'student_year': 1
        },
        {
            'major': 1,
            'title': '단일전공',
            'student_year': 2
        },
        {
            'major': 1,
            'title': '단일전공',
            'student_year': 3
        },

    ]
    MajorTrack =[
        {
            # 다전공 1전공 21학번 쭉
            'track': 1,
            'major': '경영',
            'complete_point' : 126,
            'gicho_point' : 9 ,
            'duty_point' : 15 ,
            'duty_choice_point' : 9,
            'choice_point' : 15
        },
        {
            # 다전공 타전공
            'track': 4,
            'major': '경영',
            'complete_point' : 126,
            'gicho_point' : 9 ,
            'duty_point' : 15 ,
            'duty_choice_point' : 9,
            'choice_point' : 15
        },
        {
            # 단일전공
            'track': 7,
            'major': '경영',
            'complete_point' : 126,
            'gicho_point' : 9 ,
            'duty_point' : 15 ,
            'duty_choice_point' : 9,
            'choice_point' : 15
        },
        {
            # 다전공 1전공 22 학번 쭉
            'track': 2,
            'major': '경영',
            'complete_point' : 126,
            'gicho_point' : 9 ,
            'duty_point' : 15 ,
            'duty_choice_point' : 9,
            'choice_point' : 15
        },
        {
            # 다전공 타전공
            'track': 5,
            'major': '경영',
            'complete_point' : 126,
            'gicho_point' : 9 ,
            'duty_point' : 15 ,
            'duty_choice_point' : 9,
            'choice_point' : 15
        },
        {
            # 단일전공
            'track': 8,
            'major': '경영',
            'complete_point' : 126,
            'gicho_point' : 9 ,
            'duty_point' : 15 ,
            'duty_choice_point' : 9,
            'choice_point' : 15
        },
        {
            # 다전공 1전공 23학번 쭉
            'track': 3,
            'major': '경영',
            'complete_point' : 126,
            'gicho_point' : 9 ,
            'duty_point' : 15 ,
            'duty_choice_point' : 9,
            'choice_point' : 15
        },
        {
            # 다전공 타전공
            'track': 6,
            'major': '경영',
            'complete_point' : 126,
            'gicho_point' : 9 ,
            'duty_point' : 15 ,
            'duty_choice_point' : 9,
            'choice_point' : 15
        },
        {
            # 단일전공
            'track': 9,
            'major': '경영',
            'complete_point' : 126,
            'gicho_point' : 9 ,
            'duty_point' : 15 ,
            'duty_choice_point' : 9,
            'choice_point' : 15
        }
    ]
    
    

    def handle(self, *args, **options):

        for majortech in self.MajorTech:
            MajorTech.objects.get_or_create(
                major =  Major.objects.get(title="경영"),
                title= majortech['title'], 
                
            )
            
        
            
        for track in self.Track:
            Track.objects.get_or_create(
                major =  Major.objects.get(title="경영"),
                title = track['title'],
                student_year = StudentYear.objects.get(pk=track['student_year']),
            
            )
        for majortrack in self.MajorTrack:
            MajorTrack.objects.get_or_create(
                track = Track.objects.get(pk=majortrack['track']),
                major =  Major.objects.get(title="경영"),
                complete_point = majortrack['complete_point'],
                gicho_point = majortrack['gicho_point'],
                duty_point = majortrack['duty_point'],
                duty_choice_point = majortrack['duty_choice_point'],
                choice_point = majortrack['choice_point']
            
            )
            
                        
        self.stdout.write(self.style.SUCCESS('MGTclasses initialized'))
        return 0
            