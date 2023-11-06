from django.core.management.base import BaseCommand
from ECOclasses.models import *
from Majors.models import *

class Command(BaseCommand):
    Lectures = [
        {
            'title': '회계학원론', ##
            'code':'MGT2003',
            'point': 3,
            'semester_one': 3, #6+6+7
            'semester_two': 3, #7+7+5
            'teamplay': 4,
            'grade_recommend': '1~2',
            'season_open': 1,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '필수',
            'category22_d': '필수',
            'category21_d': '필수',
            'tech': None
        },
        {
            'title': '경제수리기초', ## ## #
            'code':'ECO2003',
            'point': 3,
            'semester_one': 2, #2+2
            'semester_two': 2, #2+1
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 1,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '선택',
            'category22_d': '선택',
            'category21_d': '선택',
            'tech': None
        },
        {
            'title': '미적분학I', ##
            'code':'STS2005',
            'point': 3,
            'semester_one': 3, #14+15+15
            'semester_two': 2, #1+1+1
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 1,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '선택',
            'category22_d': '선택',
            'category21_d': '선택',
            'tech': None
        },        
        {
            'title': '미적분학II', ##
            'code':'STS2006',
            'point': 3,
            'semester_one': 2, #1+1+1
            'semester_two': 3, #11+11+10
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 1,
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category23_d': '선택',
            'category22_d': '선택',
            'category21_d': '선택',
            'tech': None
        },        
        {
            'title': '경제학원론I', ## ## ##
            'code':'ECO2001',
            'point': 3,
            'semester_one': 3, #9+7+
            'semester_two': 3, #5+2
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 1,
            'category23': '전공필수교과',
            'category22': '전공필수교과',
            'category21': '전공필수교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '경제학원론II', ## ## ##
            'code':'ECO2002',
            'point': 3,
            'semester_one': 3, #5+4+
            'semester_two': 3, #7+3
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 1,
            'category23': '전공필수교과',
            'category22': '전공필수교과',
            'category21': '전공필수교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '경제통계학', ## ## ##
            'code':'ECO2004',
            'point': 3,
            'semester_one': 3, #4+3+
            'semester_two': 2, #3+2
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 1,
            'category23': '전공필수교과',
            'category22': '전공필수교과',
            'category21': '전공필수교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '미시경제학I', ## ## ##
            'code':'ECO2006',
            'point': 3,
            # 'former': 'ECO2001, ECO2003(혹은 STS2005나 STS2006)',
            'semester_one': 3, #4+5
            'semester_two': 3, #3+3
            'teamplay': 4,
            'grade_recommend': '2',
            'season_open': 0,
            'category23': '전공필수교과',
            'category22': '전공필수교과',
            'category21': '전공필수교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '거시경제학I', ## ## ##
            'code':'ECO2007',
            'point': 3,
            # 'former': 'ECO2001, ECO2002, ECO2003(혹은 STS2005나 STS2006)',
            'semester_one': 3, #3+3+
            'semester_two': 3, #4+3
            'teamplay': 4,
            'grade_recommend': '2',
            'season_open': 1,
            'category23': '전공필수교과',
            'category22': '전공필수교과',
            'category21': '전공필수교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '계량경제학I', ## ## ##
            'code':'ECO2009', 
            'point': 3,
            # 'former': 'ECO2004 (혹은 MGT2002 또는 MAT3020 또는 MAT2410)',
            'semester_one': 3, #2+4+
            'semester_two': 3, #3+3
            'teamplay': 4,
            'grade_recommend': '2~3',
            'season_open': 0,
            'category23': '전공필수교과',
            'category22': '전공필수교과',
            'category21': '전공필수교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '금융경제학', ## ## #
            'code':'ECO3008',
            'point': 3,
            # 'former': 'ECO2006, ECO2007',
            'semester_one': 2, #1+1
            'semester_two': 1, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '국제금융론', ## # ##
            'code':'ECO3011',
            'point': 3,
            # 'former': 'ECO2007',
            'semester_one': 2, #1+1
            'semester_two': 1, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '금융시장의빅데이터분석(캡스톤디자인)', ## ## ##
            'code':'ECO3022',
            'point': 3,
            # 'former': 'ECO2001, ECO2002',
            'semester_one': 1, #1+1
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '금융정책', ## ## ##
            'code':'ECO4008',
            'point': 3,
            # 'former': 'ECO2006, ECO2007',
            'semester_one': 2, #1+1
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '파생상품시장', ## ## #
            'code':'ECO4009',
            'point': 3,
            # 'former': 'ECO2004(혹은 MGT2002나 MAT3020), ECO2006',
            'semester_one': 1, #1
            'semester_two': 1, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '국제금융시장', ## ## #
            'code':'ECO4010',
            'point': 3,
            # 'former': 'ECO2001, ECO2002',
            'semester_one': 1, #1
            'semester_two': 1, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '기업금융론', ## #0
            'code':'ECO4025',
            'point': 3,
            # 'former': 'ECO2006',
            'semester_one': 2, #1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '금융시장계량분석(캡스톤디자인)', ## ## #
            'code':'ECO4032',
            'point': 3,
            # 'former': 'ECO2009',
            'semester_one': 1, #1
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '거시경제지표분석(캡스톤디자인)',
            'code':'ECO4033',
            'point': 3,
            # 'former': 'ECO2007',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '금융경제'
        }, 
        # {
        #     'title': '금융시장행태주의분석(캡스톤디자인)',
        #     'code':'ECO4033',
        #     'point': 3,
        #     # 'former': 'ECO2001, ECO2002',
        #     'semester_one': 0, #1
        #     'semester_two': 0,
        #     'teamplay': 4,
        #     'grade_recommend': '1',
        #     'season_open': 0,
        #     'category23': '전공선택교과',
        #     'category22': '전공선택교과',
        #     'category21': '전공선택교과',
        #     'category23_d': '선택 필수',
        #     'category22_d': '선택 필수',
        #     'category21_d': '선택 필수',
        #     'tech': '금융경제'
        # }, 
        {
            'title': '국제무역론', ## ## ##
            'code':'ECO3010',
            'point': 3,
            # 'former': 'ECO2006',
            'semester_one': 1, #1
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '국제금융론', ## ## ##
            'code':'ECO3011',
            'point': 3,
            # 'former': 'ECO2007',
            'semester_one': 2, #1+1
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '개발경제학', ## # #
            'code':'ECO3012',
            'point': 3,
            # 'former': 'ECO2006, ECO2007',
            'semester_one': 2, #1+1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '국제금융시장', ## ##
            'code':'ECO4010',
            'point': 3,
            # 'former': 'ECO2001, ECO2002',
            'semester_one': 1, #1
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '한국경제론',
            'code':'ECO4014',
            'point': 3,
            # 'former': 'ECO2001, ECO2002',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
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
            'title': '오늘의중국경제',
            'code': 'CHI3037',
            'point': 3,
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
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
            'title': '다국적기업과경제분석', ##
            'code':'ECO4036',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 0,
            'semester_two': 1,
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'code':'ECO2009',
            'point': 3,
            'semester_one': 0, #2+4
            'semester_two': 0, #3+3
            'teamplay': 4,
            'grade_recommend': '2~3',
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
            'title': '경제정보분석', ## #0
            'code':'ECO2005',
            'point': 3,
            # 'former': 'ECO2004(혹은 MGT2002나 MAT3020)',
            'semester_one': 1, #1+
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '2',
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
            'title': '경제학도를위한기계학습', #0 ## ##
            'code':'ECO3025',
            'point': 3,
            'semester_one': 0,
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '2~4',
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
            'title': '경제수리통계학', ## ## #
            'code':'ECO4004',
            'point': 3,
            # 'former': 'ECO2004(혹은 MGT2002나 MAT3020)',
            'semester_one': 1, #1
            'semester_two': 1, #1+1
            'teamplay': 4,
            'grade_recommend': '3',
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
            'title': '경제수리통계학',
            'code':'ECO4004',
            'point': 3,
            # 'former': 'ECO2004(혹은 MGT2002나 MAT3020)',
            'semester_one': 1, #1
            'semester_two': 1, #1+1
            'teamplay': 4,
            'grade_recommend': '3',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '경제이론'
        }, 
        {
            'title': '응용미시계량분석', ## ##
            'code':'ECO4035',
            'point': 3,
            # 'former': 'ECO2004, ECO2006, ECO2009',
            'semester_one': 0,
            'semester_two': 1, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '응용미시계량분석',
            'code':'ECO4035',
            'point': 3,
            # 'former': 'ECO2004, ECO2006, ECO2009',
            'semester_one': 0,
            'semester_two': 1, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '산업경제'
        }, 
        {
            'title': '응용미시계량분석',
            'code':'ECO4035',
            'point': 3,
            # 'former': 'ECO2004, ECO2006, ECO2009',
            'semester_one': 0,
            'semester_two': 1, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '공공경제'
        }, 
        {
            'title': '금융시장계량분석(캡스톤디자인)', ## #0
            'code':'ECO4032',
            'point': 3,
            # 'former': 'ECO2009',
            'semester_one': 1, #1
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '고급계량경제학I', ## ## ##
            'code':'ECOG030',
            'point': 3,
            'former': 'ECO2009',
            'semester_one': 2, #1+1
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '4',
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
            'title': '거시경제지표분석(캡스톤디자인)',
            'code':'ECO4033',
            'point': 3,
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
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
            'title': '산업경제학', ## ## ##
            'code':'ECO3001',
            'point': 3,
            # 'former': 'ECO2004, ECO2006',
            'semester_one': 2, #1+1
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '기술경제학', #0 #
            'code':'ECO3003',
            'point': 3,
            # 'former': 'ECO2004(혹은 MGT2002나 MAT3020), ECO2006',
            'semester_one': 1, #1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '게임이론', ## # #
            'code':'ECO4005',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 1, #1
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '게임이론', ## #
            'code':'ECO4005',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 1, #1
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '경제이론'
        }, 
        {
            'title': '정보경제학', ## ## #
            'code':'ECO4006',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 1, 
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '정보경제학', ## ##
            'code':'ECO4006',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 1,
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '경제이론'
        }, 
        {
            'title': '경쟁법과산업규제의경제학', ## ##
            'code':'ECO4007',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 0,
            'semester_two': 1, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '기업금융론', ## #0
            'code':'ECO4025',
            'point': 3,
            # 'former': 'ECO2006',
            'semester_one': 1, #1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '공공경제학', ## # #
            'code':'ECO3009',
            'point': 3,
            # 'former': 'ECO2006, ECO2007',
            'semester_one': 2, #1+1
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '3~4',
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
            'title': '노동경제학', ## # ##
            'code':'ECO3002',
            'point': 3,
            # 'former': 'ECO2004(혹은 MGT2002나 MAT3020), ECO2006',
            'semester_one': 2, #1+1
            'semester_two': 1,
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '공공경제'
        },
        {
            'title': '도시경제학', ## ## ##
            'code':'ECO3004',
            'point': 3,
            # 'former': 'ECO2006',
            'semester_one': 2, #1+1
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '공공경제'
        },
        {
            'title': '환경경제학', ## ## ##
            'code':'ECO3005',
            'point': 3,
            # 'former': 'ECO2006, ECO2007',
            'semester_one': 0,
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '공공경제'
        },
        {
            'title': '교육경제학',
            'code':'ECO3006',
            'point': 3,
            # 'former': 'ECO2006, ECO2007',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '공공경제'
        },
        {
            'title': '농업경제학',
            'code':'ECO3007',
            'point': 3,
            # 'former': 'ECO2006',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '공공경제'
        },
        {
            'title': '개발경제학', ## ##
            'code':'ECO3012',
            'point': 3,
            # 'former': 'ECO2006, ECO2007',
            'semester_one': 2, #1+1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '공공경제'
        },
        {
            'title': '인구경제학',
            'code':'ECO3019',
            'point': 3,
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '공공경제'
        },
########################## base #################################
        {
            'title': '수리경제학', ## ##
            'code':'ECO2008',
            'point': 3,
            # 'former': 'ECO2001, ECO2003 (혹은 STS2005나 STS2006)',
            'semester_one': 2, #1+1+
            'semester_two': 1, #1+
            'teamplay': 4,
            'grade_recommend': '2',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '산업경제'
        },
        {
            'title': '수리경제학', ## #
            'code':'ECO2008',
            'point': 3,
            # 'former': 'ECO2001, ECO2003 (혹은 STS2005나 STS2006)',
            'semester_one': 2, #1+1+
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '2',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '경제이론'
        },
        {
            'title': '경제학설사I',
            'code':'ECO2010',
            'point': 3,
            # 'former': 'ECO2001, ECO2002',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '근대경제사',
            'code':'ECO2011',
            'point': 3,
            # 'former': 'ECO2001, ECO2002',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '동태계획법', #
            'code':'ECO2012',
            'point': 3,
            # 'former': 'ECO2003(혹은 STS2005나 STS2006)',
            'semester_one': 1,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '2~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '국제경제학', ## ## ##
            'code':'ECO3017',
            'point': 3,
            # 'former': 'ECO2001, ECO2002',
            'semester_one': 1,
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '글로벌경제'
        },
        {
            'title': '경제학현장실습', #0
            'code':'ECO3020',
            'point': 3,
            'former': None,
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3',
            'season_open': 1,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '경제성장론', ## #0 #
            'code':'ECO3021',
            'point': 3,
            # 'former': 'ECO2003(혹은 STS2005나 STS2006), ECO2007',
            'semester_one': 1, #1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '금융경제'
        },
        {
            'title': '경제성장론', ## #0
            'code':'ECO3021',
            'point': 3,
            # 'former': 'ECO2003(혹은 STS2005나 STS2006), ECO2007',
            'semester_one': 1, #1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '글로벌경제'
        },
        {
            'title': 'AI금융(캡스톤디자인)', ## #0 #
            'code':'ECO3023',
            'point': 3,            
            # 'former': 'ECO2001, ECO2002',
            'semester_one': 1, #1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '경제학도를위한파이썬', #0 # #
            'code':'ECO3024',
            'point': 3,
            'former': None,
            'semester_one': 1, #2+
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1~3',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '교통경제학', #0 # #
            'code':'ECO3026',
            'point': 3,
            # 'former': 'ECO2001, ECO2004',
            'semester_one': 1, #1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '주식및채권시장', #0 ## #
            'code':'ECO4037',
            'point': 3,
            # 'former': 'ECO2003, ECO2004, ECO2006',
            'semester_one': 1, #1
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '2~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '경기변동론', #0 ## ##
            'code':'ECO4038',
            'point': 3,
            'former': None,
            'semester_one': 0,
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '2~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '응용미시이론',
            'code':'ECO4039',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '미시경제학II', ## ## ##
            'code':'ECO4001',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 0, 
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '계량경제'
        },
        {
            'title': '미시경제학II',
            'code':'ECO4001',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 0,
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '공공경제'
        },
        {
            'title': '미시경제학II',
            'code':'ECO4001',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 0,
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '경제이론'
        },
        {
            'title': '거시경제학II', ## #0
            'code':'ECO4002',
            'point': 3,
            'former': 'ECO2007',
            'semester_one': 0,
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '금융경제'
        },
        {
            'title': '거시경제학II', ## #0 ##
            'code':'ECO4002',
            'point': 3,
            'former': 'ECO2007',
            'semester_one': 0,
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '글로벌경제'
        },
        {
            'title': '거시경제학II', ## #0
            'code':'ECO4002',
            'point': 3,
            'former': 'ECO2007',
            'semester_one': 0,
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '계량경제'
        },
        {
            'title': '거시경제학II', ## #0
            'code':'ECO4002',
            'point': 3,
            'former': 'ECO2007',
            'semester_one': 0,
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '경제이론'
        },
        {
            'title': '재정정책',
            'code':'ECO4011',
            'point': 3,
            # 'former': 'ECO2006, ECO2007',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '경제학특강I', ## #0
            'code':'ECO4018',
            'point': 3,
            # 'former': 'ECO2001, ECO2002',
            'semester_one': 1, #1
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '2~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '경제학특강II',
            'code':'ECO4019',
            'point': 3,
            # 'former': 'ECO2001, ECO2002',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '경제학특강III',
            'code':'ECO4020',
            'point': 3,
            # 'former': 'ECO2001, ECO2002',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '경제학특강IV',
            'code':'ECO4021',
            'point': 3,
            # 'former': 'ECO2001, ECO2002',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '경제학특강V',
            'code':'ECO4022',
            'point': 3,
            # 'former': 'ECO2001, ECO2002',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '경제학세미나',
            'code':'ECO4023',
            'point': 3,
            # 'former': 'ECO2006, ECO2007',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '경제학방법론', #0 #
            'code':'ECO4029',
            'point': 3,
            # 'former': 'ECO2004(혹은 MGT2002나 MAT3020)',
            'semester_one': 1, #1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '행동경제학', ## # #0
            'code':'ECO4030',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 1, #1+1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '금융경제'
        },
        {
            'title': '행동경제학', ## #
            'code':'ECO4030',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 1, #1+1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '산업경제'
        },
        {
            'title': '행동경제학', ## #
            'code':'ECO4030',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 1, #1+1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '경제이론'
        },
        {
            'title': '실험경제학', ## ## ##
            'code':'ECO4031',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 0,
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '2~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '산업경제'
        },
        {
            'title': '실험경제학', ## ## ##
            'code':'ECO4031',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 0,
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '2~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '경제이론'
        },
        {
            'title': '고급미시경제학I', ## # ##
            'code':'ECOG010',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 2, #1+1
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '경제이론'
        },
        {
            'title': '고급미시경제이론',
            'code':'ECOG011',
            'point': 3,
            'former': 'ECO2006',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '고급거시경제학I', ## ## ##
            'code':'ECOG020',
            'point': 3,
            # 'former': 'ECO2006, ECO2007',
            'semester_one': 2, #1+1
            'semester_two': 2, #1+1
            'teamplay': 4,
            'grade_recommend': '4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': '경제이론'
        },
        {
            'title': '고급거시경제이론',
            'code':'ECOG021',
            'point': 3,
            # 'former': 'ECO2006, ECO2007',
            'semester_one': 0,
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '1',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '고급수리통계학', ## # #
            'code':'ECOG040',
            'point': 3,
            'former': None,
            'semester_one': 2, #1+1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': 'AI와빅데이터를활용한경제정보처리', #0 ## #
            'code':'ECOG051',
            'point': 3,
            'semester_one': 1, #1
            'semester_two': 1, #1
            'teamplay': 4,
            'grade_recommend': '2~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': None,
            'category22_d': None,
            'category21_d': None,
            'tech': None
        },
        {
            'title': '금융시장행태주의(behavioral)분석(캡스톤디자인)', ## #0
            'code':'ECO4034',
            'point': 3,
            # 'former': 'ECO2001, ECO2002'
            'semester_one': 1, #1
            'semester_two': 0,
            'teamplay': 4,
            'grade_recommend': '3~4',
            'season_open': 0,
            'category23': '전공선택교과',
            'category22': '전공선택교과',
            'category21': '전공선택교과',
            'category23_d': '선택 필수',
            'category22_d': '선택 필수',
            'category21_d': '선택 필수',
            'tech': '금융경제'
        },
    ]

    def handle(self, *args, **options):
        for data in self.Lecture:
                if 'former' not in data:
                    data['former'] = None
        for lecture in self.Lectures:
            lec = Lecture(
            title = lecture['title'], 
            label = lecture['title'],
            former = lecture['former'],
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
            

            lec.save()
        self.stdout.write(self.style.SUCCESS('Lectures initialized'))
        return 0