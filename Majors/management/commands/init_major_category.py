from django.core.management.base import BaseCommand
from Majors.models import *
class Command(BaseCommand):
    help = 'Initialize Major, Category'
    Major = [  
        {
            'title': '경영',
            
        }, 
        {
            'title': '컴퓨터공학',
            
        }, 
        {
            'title': '경제',
            
        }, 
    ]
    
    Category = [
        {
            'title': '공통필수교과',
            'detail': '서강인성',
            'duty_point': 1
        },
        {
            'title': '공통필수교과',
            'detail': '글쓰기',
            'duty_point': 3
        },
        {
            'title': '공통필수교과',
            'detail': '글로벌 언어1',
            'duty_point': 3
        },
        {
            'title': '공통필수교과',
            'detail': '전공 진로 탐색',
            'duty_point': 1
        },
        {
            'title': '공통필수교과',
            'detail': '소프트웨어',
            'duty_point': 3
        },
        {
            'title': '공통선택교과',
            'detail': '인간과 신앙',
            'duty_point': 3
        },
        {
            'title': '공통선택교과',
            'detail': '인간과 사상',
            'duty_point': 3
        },
        {
            'title': '공통선택교과',
            'detail': '인간과 사회',
            'duty_point': 3
        },
        {
            'title': '공통선택교과',
            'detail': '인간과 과학',
            'duty_point': 3
        },
        {
            'title': '전공입문교과',
            'detail': None,
            'duty_point': 3
        },
        {
            'title': '전공필수교과',
            'detail': None,
            'duty_point': 3
        },
        {
            'title': '전공선택교과',
            'detail': None,
            'duty_point': 3
        },
    ]

    def handle(self, *args, **options):
        for major in self.Major:
            Major.objects.get_or_create(
                title = major['title'], 
                
            )
            
        # for category in self.Category:
        #     cate = Category(
        #         title = category['title'],
        #         duty_point = category['duty_point']
        #     )
        #     if category['detail'] is not None:
        #         cate.detail = category ['detail']
        #     cate.save()
                        
        self.stdout.write(self.style.SUCCESS('Major&Category initialized'))
        return 0
            