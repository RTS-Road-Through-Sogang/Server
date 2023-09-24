from django.core.management.base import BaseCommand
from Majors.models import *
from CSEclasses.models import *

class Command(BaseCommand):
    Lectures = [
        {   'title': '미적분학1',
            'code':'STS2005',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 1,
            'former': None,
            'grade_recommend': 1,
            'season_open': 1,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '필수',
            'category22_d': '필수',
            'category21_d': '필수',
            'tech' : None
        },
        {   'title': '미적분학2',
            'code':'STS2006',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 1,
            'former': None,
            'grade_recommend': 1,
            'season_open': 1,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '필수',
            'category22_d': '필수',
            'category21_d': '필수',
            'tech' : None
        },
        {   'title': '일반물리실험1',
            'code':'PHY1101',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 1,
            'former': None,
            'grade_recommend': 1,
            'season_open': 1,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '필수',
            'category22_d': '필수',
            'category21_d': '필수',
            'tech' : None
        },
        {   'title': '일반물리1',
            'code':'PHY1001',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 1,
            'former': None,
            'grade_recommend': 1,
            'season_open': 1,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '필수',
            'category22_d': '필수',
            'category21_d': '필수',
            'tech' : None
        },
        {   'title': '응용수학1',
            'code':'MAT2410',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 1,
            'former': None,
            'grade_recommend': 1,
            'season_open': 1,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '필수',
            'category22_d': '필수',
            'category21_d': '필수',
            'tech' : None
        },
        {   'title': '응용수학2',
            'code':'MAT2420',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 1,
            'former': None,
            'grade_recommend': 1,
            'season_open': 1,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '필수',
            'category22_d': '필수',
            'category21_d': '필수',
            'tech' : None
        },
        
    ]
    def handle(self, *args, **options):
        for lecture in self.Lectures:
            lec = Lecture(
            title = lecture['title'], 
            code = lecture['code'], 
            point = lecture['point'], 
            semester_one = lecture['semester_one'], 
            semester_two = lecture['semester_two'], 
            teamplay = lecture['teamplay'], 
            season_open = lecture['season_open'], 
            grade_recommend = lecture['grade_recommend'], 
            category23 = Category.objects.get( title = lecture['category23'], detail = lecture['category23_d']),
            category22 = Category.objects.get( title = lecture['category22'], detail = lecture['category22_d']),            
            category21 = Category.objects.get( title = lecture['category21'], detail = lecture['category21_d']),
            teach = 0,
            advance = 0
            )
            if (lecture['tech']) is not None:
                lec.tech = MajorTech.objects.get( title = lecture['tech'])
            former_title = lecture.get('former')

            if former_title:
                    try:
                        lec.former = Lecture.objects.get(title=former_title)
                    except Lecture.DoesNotExist:
                        pass
            lec.save()
        self.stdout.write(self.style.SUCCESS('Lectures initialized'))
        return 0