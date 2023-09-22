from django.core.management.base import BaseCommand
from ECOclasses.models import *
from Majors.models import *
class Command(BaseCommand):

    help = 'Initialize , Category'
    MajorTech = [  
        {

            'title' : '금융경제'
            
        }, 
        {
            'title' : '글로벌경제'
            
        }, 
        {
            'title' : '계량경제'
            
        }, 
        {
            'title' : '산업경제'
            
        }, 
        {
            'title' : '공공경제'
            
        }, 
        {
            'title' : '경제이론'
            
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
                {
            'major': 1,
            'title': 'Honors Program',
            'student_year': 1
        },
                {
            'major': 1,
            'title': 'Honors Program',
            'student_year': 2
        },
                {
            'major': 1,
            'title': 'Honors Program',
            'student_year': 3
        },
        
    ]

    def handle(self, *args, **options):

        for majortech in self.MajorTech:
            MajorTech.objects.get_or_create(
                major =  Major.objects.get(title="경제"),
                title= majortech['title'], 
                
            )
            
        
            
        for track in self.Track:
            Track.objects.get_or_create(
                major =  Major.objects.get(title="경제"),
                title = track['title'],
                student_year = StudentYear.objects.get(pk=track['student_year']),
            
            )
            
                        
        self.stdout.write(self.style.SUCCESS('ECOclasses initialized'))
        return 0
            