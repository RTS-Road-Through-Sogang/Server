from django.core.management.base import BaseCommand
from ECOclasses.models import *
from Majors.models import *

class Command(BaseCommand):
    Lectures = [
        {
            'title': '회계학원론',
            'code':'MGT2003',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '필수',
            'category22_d': '필수',
            'category21_d': '필수'
        },
        {
            'title': '경제수리기초',
            'code':'ECO2003',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '선택',
            'category22_d': '선택',
            'category21_d': '선택'
        },
        {
            'title': '미적분학 I',
            'code':'STS2005',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '선택',
            'category22_d': '선택',
            'category21_d': '선택'
        },        
        {
            'title': '미적분학 II',
            'code':'STS2006',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '선택',
            'category22_d': '선택',
            'category21_d': '선택'
        },        
        {
            'title': '경제학원론 I',
            'code':'ECO2001',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공필수교과',
            'category22': '전공필수교과',
            'category21': '전공필수교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None
        },
        {
            'title': '경제학원론 II',
            'code':'ECO2002',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공필수교과',
            'category22': '전공필수교과',
            'category21': '전공필수교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None
        },
        {
            'title': '금융경제학',
            'code':'ECO3008',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '필수',
            'category22_d': '필수',
            'category21_d': '필수',
            'tech': '금융경제'
        }, 
        {
            'title': '국제금융론',
            'code':'ECO3011',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '금융경제'
        }, 
        {
            'title': '국제무역론',
            'code':'ECO3010',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '필수',
            'category22_d': '필수',
            'category21_d': '필수',
            'tech': '글로벌경제'
        }, 
        {
            'title': '개발경제학',
            'code':'ECO3012',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '글로벌경제'
        }, 
        {
            'title': '계랑경제학I',
            'code':'ECO',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '필수',
            'category22_d': '필수',
            'category21_d': '필수',
            'tech': '계량경제'
        }, 
        {
            'title': '경제정보분석',
            'code':'ECO2005',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '계량경제'
        }, 
        {
            'title': '산업경제학',
            'code':'ECO3001',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '필수',
            'category22_d': '필수',
            'category21_d': '필수',
            'tech': '산업경제'
        }, 
        {
            'title': '기술경제학',
            'code':'ECO3003',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '산업경제'
        }, 
        {
            'title': '공공경제학',
            'code':'ECO3009',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '필수',
            'category22_d': '필수',
            'category21_d': '필수',
            'tech': '공공경제'
        }, 
        {
            'title': '노동경제학',
            'code':'ECO3002',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 4,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '공공경제'
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
            tech = MajorTech.objects.get(title = lecture['tech'])
            )
            lec.save()
        self.stdout.write(self.style.SUCCESS('Lectures initialized'))
        return 0