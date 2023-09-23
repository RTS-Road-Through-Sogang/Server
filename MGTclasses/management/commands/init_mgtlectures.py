from django.core.management.base import BaseCommand
from MGTclasses.models import *
from Majors.models import *

class Command(BaseCommand):    
    Lecture =[ 
                
                
                {
                    'title': '경제학원론 I',
                    'code':'ECO2001',
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
                    'category21_d': '선택',
                    'tech': None
                },
                {
                    'title': '경영통계학',
                    'code':'ECO2001',
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
                    'category21_d': '선택',
                    'tech': None
                },
                {
                    'title': '대학수학',
                    'code':'ECO2001',
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
                    'category21_d': '선택',
                    'tech': None
                },
                {
                    'title': '관리회계',
                    'code':'ECO2001',
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
                    'tech': '회계'
                },
                {
                    'title': '마케팅원론',
                    'code':'MGT3009',
                    'point': 3,
                    'semester_one': 3,
                    'semester_two': 3,
                    'teamplay': 4,
                    'grade_recommend': 2,
                    'season_open': 0,
                    'category23': '전공필수교과',
                    'category22': '전공필수교과',
                    'category21': '전공필수교과',
                    'category23_d': None,
                    'category22_d': None,
                    'category21_d': None,
                    'tech': '마케팅'
                }, 
                {
                    'title': '조직행동이론',
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
                    'category21_d': None,
                    'tech': '인사조직'
                },
                {
                    'title': '재무관리',
                    'code':'EC2O2001',
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
                    'category21_d': None,
                    'tech': '재무보험'
                },
                {
                    'title': '생산관리론',
                    'code':'MGT3009',
                    'point': 3,
                    'semester_one': 3,
                    'semester_two': 3,
                    'teamplay': 4,
                    'grade_recommend': 2,
                    'season_open': 0,
                    'category23': '전공필수교과',
                    'category22': '전공필수교과',
                    'category21': '전공필수교과',
                    'category23_d': None,
                    'category22_d': None,
                    'category21_d': None,
                    'tech': '국제경영'
                }, 
                {
                    'title': '회계학원론',
                    'code':'MGT3009',
                    'point': 3,
                    'semester_one': 3,
                    'semester_two': 3,
                    'teamplay': 4,
                    'grade_recommend': 2,
                    'season_open': 0,
                    'category23': '전공필수교과',
                    'category22': '전공필수교과',
                    'category21': '전공필수교과',
                    'category23_d': None,
                    'category22_d': None,
                    'category21_d': None,
                    'tech': '회계'
                }, 
                {
                    'title': '경영정보시스템',
                    'code':'MGT3009',
                    'point': 3,
                    'semester_one': 3,
                    'semester_two': 3,
                    'teamplay': 2,
                    'grade_recommend': 2,
                    'season_open': 0,
                    'category23': '전공선택교과',
                    'category22': '전공선택교과',
                    'category21': '전공선택교과',
                    'category23_d': '필수',
                    'category22_d': '필수',
                    'category21_d': '필수',
                    'tech': 'BA/LSOM/MIS'
                },
                {
                    'title': '인적자원관리',
                    'code':'MGT3009',
                    'point': 3,
                    'semester_one': 3,
                    'semester_two': 3,
                    'teamplay': 2,
                    'grade_recommend': 2,
                    'season_open': 0,
                    'category23': '전공선택교과',
                    'category22': '전공선택교과',
                    'category21': '전공선택교과',
                    'category23_d': '필수',
                    'category22_d': '필수',
                    'category21_d': '필수',
                    'tech': '인사조직',
                    'former' : '조직행동이론',
                }, 
                {
                    'title': 'CEO 경영특강',
                    'code':'MGT3009',
                    'point': 3,
                    'semester_one': 3,
                    'semester_two': 3,
                    'teamplay': 2,
                    'grade_recommend': 2,
                    'season_open': 0,
                    'category23': '전공선택교과',
                    'category22': '전공선택교과',
                    'category21': '전공선택교과',
                    'category23_d': None,
                    'category22_d': None,
                    'category21_d': None,
                    'tech': '기타'
                } 
            ]
    def handle(self, *args, **options):
            i=0
            for lecture in self.Lecture:
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
                
            self.stdout.write(self.style.SUCCESS('MGT Lectures initialized'))
            return 0