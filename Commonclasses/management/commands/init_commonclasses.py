from django.core.management.base import BaseCommand
from Commonclasses.models import *
from Majors.models import *

class Command(BaseCommand):
    Lectures = [
        {
            'title': '성찰과성장',
            'code':'COR1007',
            'point': 1,
            'semester_one': 1+10+11,
            'semester_two': 5+20,
            'teamplay': 5,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '서강인성',
            'category22': '서강인성',
            'category21': '서강인성'
        },
        {   'title': '인문사회글쓰기', ## #
            'code':'COR1012',
            'point': 3,
            'semester_one': 19+19+17,
            'semester_two': 16+17+17,
            'teamplay': 1, 
            'grade_recommend': '3',
            'season_open': 1, #
            'category23': '글쓰기',
            'category22': '글쓰기',
            'category21': '글쓰기'
        },
        {   'title': '자연계글쓰기', ## #
            'code':'COR1013',
            'point': 3,
            'semester_one': 12+11+10,
            'semester_two': 11+9+10,
            'teamplay': 3,
            'grade_recommend': '1',
            'season_open': 1, #
            'category23': '글쓰기',
            'category22': '글쓰기',
            'category21': '글쓰기'
        },
        {   'title': '영어글로벌의사소통I', ## #
            'code':'COR1003',
            'point': 3,
            'semester_one': 33+31+24,
            'semester_two': 22+19+17,
            'teamplay': 4,
            'grade_recommend': '1', 
            'season_open': 1, #
            'category23': '글로벌 언어I',
            'category22': '글로벌 언어I',
            'category21': '글로벌 언어I'
        },
        {   'title': '독일언어와문화I',
            'code':'LCS2001',
            'point': 3,
            'semester_one': 7+6+5,
            'semester_two': 4+4+5,
            'teamplay': 1,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '글로벌 언어I',
            'category22': '글로벌 언어I',
            'category21': '글로벌 언어I'
        },
        {   'title': '프랑스언어와문화I',
            'code':'LCS2003',
            'point': 3,
            'semester_one': 6+5+6,
            'semester_two': 4+5+5,
            'teamplay': 2,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '글로벌 언어I',
            'category22': '글로벌 언어I',
            'category21': '글로벌 언어I'
        },
        {   'title': '중국언어와문화I',
            'code':'LCS2005',
            'point': 3,
            'semester_one': 6+4+4,
            'semester_two': 4+4+4,
            'teamplay': 2,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '글로벌 언어I',
            'category22': '글로벌 언어I',
            'category21': '글로벌 언어I'
        },
        {   'title': '일본언어와문화I',
            'code':'LCS2007',
            'point': 3,
            'semester_one': 6+6+4,
            'semester_two': 6+4+4,
            'teamplay': 1,
            'grade_recommend': '1~4',
            'season_open': 0,
            'category23': '글로벌 언어I',
            'category22': '글로벌 언어I',
            'category21': '글로벌 언어I'
        },
        {   'title': '초급라틴어', ## ## ##
            'code':'LCU4021',
            'point': 3,
            'semester_one': 1+1,
            'semester_two': 1,
            'teamplay': 1,
            'grade_recommend': '1~4',
            'season_open': 0,
            'category23': '글로벌 언어I',
            'category22': '글로벌 언어I',
            'category21': '글로벌 언어I'
        },
        {   'title': '초급스페인어',
            'code':'LCU4030',
            'point': 3,
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 1,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '글로벌 언어I',
            'category22': '글로벌 언어I',
            'category21': '글로벌 언어I'
        },
        {   'title': '초급이탈리아어',
            'code':'LCU4025',
            'point': 3,
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 1,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '글로벌 언어I',
            'category22': '글로벌 언어I',
            'category21': '글로벌 언어I'
        },
        {   'title': '초급러시아어', ## ## ##
            'code':'LCU4035',
            'point': 3,
            'semester_one': 1+1+1,
            'semester_two': 1+1+1,
            'teamplay': 1,
            'grade_recommend': '1~4',
            'season_open': 0,
            'category23': '글로벌 언어I',
            'category22': '글로벌 언어I',
            'category21': '글로벌 언어I'
        },
        {   'title': '초급아랍어', ## ## ##
            'code':'LCU4105',
            'point': 3,
            'semester_one': 1+1+1,
            'semester_two': 1+1+1,
            'teamplay': 1,
            'grade_recommend': '1~4',
            'season_open': 0,
            'category23': '글로벌 언어I',
            'category22': '글로벌 언어I',
            'category21': '글로벌 언어I'
        },
        
        {   'title': '알바트로스세미나',
            'code':'COR1015',
            'point': 3,
            'semester_one': 79+31+34,
            'semester_two': 1,
            'teamplay': 1,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공 진로 탐색',
            'category22': '전공 진로 탐색',
            'category21': '전공 진로 탐색'
        },
        {   'title': '알바트로스세미나(경영)',
            'code':'COR1016',
            'point': 3,
            'semester_one': 40+7+10,
            'semester_two': 0,
            'teamplay': 1,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공 진로 탐색',
            'category22': '전공 진로 탐색',
            'category21': '전공 진로 탐색'
        },
        {   'title': '기초인공지능프로그래밍(구 컴퓨팅사고력)', ## #
            'code':'COR1010',
            'point': 3,
            'semester_one': 14+9+12,
            'semester_two': 5+10+12,
            'teamplay': 1,
            'grade_recommend': '1',
            'season_open': 1, #
            'category23': '소프트웨어',
            'category22': '소프트웨어',
            'category21': None
        },
        # {   'title': '기초인공지능프로그래밍 고급(구 컴퓨팅사고력 고급)',
        #     'code':'COR1010',
        #     'point': 3,
        #     'semester_one': 3,
        #     'semester_two': 3,
        #     'teamplay': 1,
        #     'grade_recommend': 1,
        #     'season_open': 1,
        #     'category23': '소프트웨어',
        #     'category22': '소프트웨어',
        #     'category21': None
        # },
        {   'title': '철학적인간학', ## #
            'code':'HFS2001',
            'point': 3,
            'semester_one': 5+6+6,
            'semester_two': 5+5+5,
            'teamplay': 1,
            'grade_recommend': '2',
            'season_open': 1, #
            'category23': '인간과 신앙',
            'category22': '인간과 신앙',
            'category21': '인간과 신앙'
        },
        {   'title': '신학적인간학', ## #
            'code':'HFS2002',
            'point': 3,
            'semester_one': 5+5+6,
            'semester_two': 2+2+4,
            'teamplay': 3,
            'grade_recommend': '2',
            'season_open': 1, #
            'category23': '인간과 신앙',
            'category22': '인간과 신앙',
            'category21': '인간과 신앙'
        },
        {   'title': '그리스도교윤리', ## #
            'code':'HFS2003',
            'point': 3,
            'semester_one': 5+4+4,
            'semester_two': 5+4+3,
            'teamplay': 3,
            'grade_recommend': '2',
            'season_open': 1, ##
            'category23': '인간과 신앙',
            'category22': '인간과 신앙',
            'category21': '인간과 신앙'
        },
        {   'title': '그리스도교신앙과 영성', ## 
            'code':'HFU4012',
            'point': 3,
            'semester_one': 0,
            'semester_two': 1+1+1,
            'teamplay': 1,
            'grade_recommend': 1,
            'season_open': 0,
            'category23': '인간과 신앙',
            'category22': '인간과 신앙',
            'category21': '인간과 신앙'
        },
        {   'title': '진선미성', ## #
            'code':'HFU4023',
            'point': 3,
            'semester_one': 2+2+2,
            'semester_two': 2+2+2,
            'teamplay': 3,
            'grade_recommend': '2~4',
            'season_open': 0,
            'category23': '인간과 신앙',
            'category22': '인간과 신앙',
            'category21': '인간과 신앙'
        },
        {   'title': '현대세계와윤리문제', ## #
            'code':'ETS2001',
            'point': 3,
            'semester_one': 4+5+4,
            'semester_two': 4+1+3,
            'teamplay': 1,
            'grade_recommend': '1~4',
            'season_open': 1, #
            'category23': '인간과 사상',
            'category22': '인간과 사상',
            'category21': '인간과 사상'
        },
        {   'title': '논리와비판적사고', ## #
            'code':'ETS2002', 
            'point': 3,
            'semester_one': 6+5+4,
            'semester_two': 4+4+4,
            'teamplay': 1,
            'grade_recommend': '1~4',
            'season_open': 1, #
            'category23': '인간과 사상',
            'category22': '인간과 사상',
            'category21': '인간과 사상'
        },
        {   'title': '종교와세계문화', ## #
            'code':'ETS2004',
            'point': 3,
            'semester_one': 7+7+7,
            'semester_two': 2+5+4,
            'teamplay': 1,
            'grade_recommend': '1~4',
            'season_open': 1, #
            'category23': '인간과 사상',
            'category22': '인간과 사상',
            'category21': '인간과 사상'
        },
        {   'title': '현대한국의형성', ## ## ##
            'code':'CHS2002',
            'point': 3,
            'semester_one': 5+3+4,
            'semester_two': 5+5+4,
            'teamplay': 1,
            'grade_recommend': '1~2',
            'season_open': 1, #
            'category23': '인간과 사상',
            'category22': '인간과 사상',
            'category21': '인간과 사상'
        },
        {   'title': '현대동아시아의형성', ## ## ##
            'code':'CHS2003',
            'point': 3,
            'semester_one': 2+2+2,
            'semester_two': 3+2+2,
            'teamplay': 1,
            'grade_recommend': '1~2',
            'season_open': 1, #
            'category23': '인간과 사상',
            'category22': '인간과 사상',
            'category21': '인간과 사상'
        },
        {   'title': '현대서양의형성', ## ## ##
            'code':'CHS2004',
            'point': 3,
            'semester_one': 2+2+2,
            'semester_two': 1+1+2,
            'teamplay': 3,
            'grade_recommend': '1~2',
            'season_open': 1, #
            'category23': '인간과 사상',
            'category22': '인간과 사상',
            'category21': '인간과 사상'
        },
        {   'title': '현대사회의이해', ## ## ##
            'code':'SHS2001',
            'point': 3,
            'semester_one': 2+2+2,
            'semester_two': 2+2+2,
            'teamplay': 1,
            'grade_recommend': '1~2',
            'season_open': 1, ###
            'category23': '인간과 사회',
            'category22': '인간과 사회',
            'category21': '인간과 사회'
        },
        {   'title': '한국과세계', ## ## ##
            'code':'SHS2002',
            'point': 3,
            'semester_one': 4+4+4,
            'semester_two': 3+4+4,
            'teamplay': 1,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '인간과 사회',
            'category22': '인간과 사회',
            'category21': '인간과 사회'
        },
        {   'title': '커뮤니케이션과사회', ## ## ##
            'code':'SHS2003',
            'point': 3,
            'semester_one': 1+1+1,
            'semester_two': 1+1+1,
            'teamplay': 1,
            'grade_recommend': '1~4',
            'season_open': 1, #
            'category23': '인간과 사회',
            'category22': '인간과 사회',
            'category21': '인간과 사회'
        },
        {   'title': '생활속의심리학', ## ## ##
            'code':'SHS2007',
            'point': 3,
            'semester_one': 4+3+3,
            'semester_two': 3+3+3,
            'teamplay': 3,
            'grade_recommend': '1~4',
            'season_open': 1, ##
            'category23': '인간과 사회',
            'category22': '인간과 사회',
            'category21': '인간과 사회'
        },
        {   'title': '법과지식재산(구 법과지식산업)', ## ## ##
            'code':'SHS2005',
            'point': 3,
            'semester_one': 5+5+5,
            'semester_two': 5+5+5,
            'teamplay': 1,
            'grade_recommend': '1~2',
            'season_open': 1, ###
            'category23': '인간과 사회',
            'category22': '인간과 사회',
            'category21': '인간과 사회'
        },
        {   'title': '자연과인간', ## ## ##
            'code':'STS2001', 
            'point': 3,
            'semester_one': 1+1+1,
            'semester_two': 1+1+1,
            'teamplay': 1,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '인간과 과학',
            'category22': '인간과 과학',
            'category21': '인간과 과학'
        },
        {   'title': '생명과환경', ## ## ##
            'code':'STS2002',
            'point': 3,
            'semester_one': 4+4+4,
            'semester_two': 2+3+3,
            'teamplay': 1,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '인간과 과학',
            'category22': '인간과 과학',
            'category21': '인간과 과학'
        },
        {   'title': '우주와원자시대', ## ## ##
            'code':'STU4011',
            'point': 3,
            'semester_one': 2+2+2,
            'semester_two': 2+3+2,
            'teamplay': 1,
            'grade_recommend': '1~4',
            'season_open': 1, #
            'category23': '인간과 과학',
            'category22': '인간과 과학',
            'category21': '인간과 과학'
        },
        {   'title': '기초빅데이터프로그래밍', ## ## ##
            'code':'STS2011',
            'point': 3,
            'semester_one': 2+2+2,
            'semester_two': 3+2+2,
            'teamplay': 1,
            'grade_recommend': '2~4',
            'season_open': 0,
            'category23': '인간과 과학',
            'category22': '인간과 과학',
            'category21': '인간과 과학'
        },
        {   'title': '딥러닝기반빅데이터처리실습', #0 # #0
            'code':'STS2012',
            'point': 3,
            'semester_one': 0,
            'semester_two': 1,
            'teamplay': 1,
            'grade_recommend': '2~4',
            'season_open': 0,
            'category23': '인간과 과학',
            'category22': '인간과 과학',
            'category21': None
        },
        {   'title': '과학사', ## ## ##
            'code':'STS2010',
            'point': 3,
            'semester_one': 2+1+1,
            'semester_two': 2+1+1,
            'teamplay': 1,
            'grade_recommend': '1~2',
            'season_open': 1, #
            'category23': '인간과 과학',
            'category22': '인간과 과학',
            'category21': '인간과 과학'
        },
        {   'title': '미적분학I', ## ## ##
            'code':'STS2005',
            'point': 3,
            'semester_one': 44,
            'semester_two': 3,
            'teamplay': 1,
            'grade_recommend': '1',
            'season_open': 1, #
            'category23': '인간과 과학',
            'category22': '인간과 과학',
            'category21': '인간과 과학'
        },
    ]

    def handle(self, *args, **options):
        for data in self.Lectures:
            a = data['title']
            if 'eta' not in data:
                data['eta'] = f"https://everytime.kr/lecture/search?keyword={a}&condition=name"
        for data in self.Lectures:  # 수정된 부분
            lec = Lecture(
                label = data['title'],
                title = data['title'], 
                code = data['code'], 
                point = data['point'], 
                eta = data['eta'],
                semester_one = data['semester_one'], 
                semester_two = data['semester_two'], 
                teamplay = data['teamplay'], 
                season_open = data['season_open'], 
                grade_recommend = data['grade_recommend'], 
                category23 = Category.objects.get( detail = data['category23']),
                category22 = Category.objects.get( detail = data['category22'])            
            )
            if data['category21'] is not None:
                lec.category21 = Category.objects.get( detail = data['category21'])
            lec.save()
        self.stdout.write(self.style.SUCCESS('Lectures initialized'))
        return 0