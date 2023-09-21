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
            'title' : '재무보험'
            
        }, 
        {
            'title' : '인사조직'
            
        }, 
        {
            'title' : '마케팅'
            
        }, 
        {
            'title' : 'BA/LSOM/MIS'
            
        }, 
        {
            'title' : '국제경영'
            
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
            'title': '다전공 2전공',
            'student_year': 1
        },
        {
            'major': 1,
            'title': '다전공 2전공',
            'student_year': 2
        },
        {
            'major': 1,
            'title': '다전공 2전공',
            'student_year': 3
        },
        {
            'major': 1,
            'title': '심화',
            'student_year': 1
        },
        {
            'major': 1,
            'title': '심화',
            'student_year': 2
        },
        {
            'major': 1,
            'title': '심화',
            'student_year': 3
        },
        {
            'major': 1,
            'title': '교육',
            'student_year': 1
        },
        {
            'major': 1,
            'title': '교육',
            'student_year': 2
        },
        {
            'major': 1,
            'title': '교육',
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
             
                        
        self.stdout.write(self.style.SUCCESS('MGTclasses initialized'))
        return 0
            