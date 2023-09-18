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
            'major': '경제',
            'title':'단일전공',
            'student_year': 23
        },
        {
            'major': '경제',
            'title':'다전공 1전공',
            'student_year': 23
        },
        {
            'major': '경제',
            'title':'다전공 타전공',
            'student_year': 23
        },
        {
            'major': '경영',
            'title':'단일전공',
            'student_year': 23
        },
        {
            'major': '경영',
            'title':'다전공 1전공',
            'student_year': 23
        },
        {
            'major': '경영',
            'title':'다전공 전공',
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
            'major': '경제',
            'title':'단일전공',
            'student_year': 22
        },
        {
            'major': '경제',
            'title':'다전공 1전공',
            'student_year': 22
        },
        {
            'major': '경제',
            'title':'다전공 타전공',
            'student_year': 22
        },
        {
            'major': '경영',
            'title':'단일전공',
            'student_year': 22
        },
        {
            'major': '경영',
            'title':'다전공 1전공',
            'student_year': 22
        },
        {
            'major': '경영',
            'title':'다전공 전공',
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
        {
            'major': '경제',
            'title':'단일전공',
            'student_year': 21
        },
        {
            'major': '경제',
            'title':'다전공 1전공',
            'student_year': 21
        },
        {
            'major': '경제',
            'title':'다전공 타전공',
            'student_year': 21
        },
        {
            'major': '경영',
            'title':'단일전공',
            'student_year': 21
        },
        {
            'major': '경영',
            'title':'다전공 1전공',
            'student_year': 21
        },
        {
            'major': '경영',
            'title':'다전공 전공',
            'student_year': 21
        },
        {
            'major': '컴퓨터공학',
            'title':'단일전공',
            'student_year': 20
        },
        {
            'major': '컴퓨터공학',
            'title':'융합과정',
            'student_year': 20
        },
        {
            'major': '컴퓨터공학',
            'title':'다전공 1전공',
            'student_year': 20
        },
        {
            'major': '컴퓨터공학',
            'title':'다전공 타전공',
            'student_year': 20
        },
        {
            'major': '컴퓨터공학',
            'title':'교직과정',
            'student_year': 20
        },
        {
            'major': '경제',
            'title':'단일전공',
            'student_year': 20
        },
        {
            'major': '경제',
            'title':'다전공 1전공',
            'student_year': 23
        },
        {
            'major': '경제',
            'title':'다전공 타전공',
            'student_year': 20
        },
        {
            'major': '경영',
            'title':'단일전공',
            'student_year': 20
        },
        {
            'major': '경영',
            'title':'다전공 1전공',
            'student_year': 20
        },
        {
            'major': '경영',
            'title':'다전공 전공',
            'student_year': 20
        },
                {
            'major': '컴퓨터공학',
            'title':'단일전공',
            'student_year': 19
        },
        {
            'major': '컴퓨터공학',
            'title':'융합과정',
            'student_year': 19
        },
        {
            'major': '컴퓨터공학',
            'title':'다전공 1전공',
            'student_year': 19
        },
        {
            'major': '컴퓨터공학',
            'title':'다전공 타전공',
            'student_year': 19
        },
        {
            'major': '컴퓨터공학',
            'title':'교직과정',
            'student_year': 19
        },
        {
            'major': '경제',
            'title':'단일전공',
            'student_year': 19
        },
        {
            'major': '경제',
            'title':'다전공 1전공',
            'student_year': 19
        },
        {
            'major': '경제',
            'title':'다전공 타전공',
            'student_year': 19
        },
        {
            'major': '경영',
            'title':'단일전공',
            'student_year': 19
        },
        {
            'major': '경영',
            'title':'다전공 1전공',
            'student_year': 19
        },
        {
            'major': '경영',
            'title':'다전공 전공',
            'student_year': 19
        },
    ]
    majortecks = [
        {
            'major': '경제',
            'title': '금융경제',
        },
        {
            'major': '경제',
            'title': '글로벌경제',
        },
        {
            'major': '경제',
            'title': '글로벌경제',
        },
        {
            'major': '경제',
            'title': '계량경제',
        },
        {
            'major': '경제',
            'title': '산업경제',
        },
        {
            'major': '경제',
            'title': '공공경제',
        },
        {
            'major': '경제',
            'title': '경제이론',
        },
        
    ]
    majortracks = [
        
    ]
    lectures = [
        {   'title': '미적분학1',
            'code':'STS2005',
            'point': 3,
            'semester_one': 3,
            'semester_two': 3,
            'teamplay': 1,
            'former': None,
            'grade_recommend': 1,
            'season_open': 1,
            'category23': '인간과 과학',
            'category22': '인간과 과학',
            'category21': '인간과 과학',
            'category20': '인간과 과학',
            'category19': '인간과 과학'
        },
    ]
    
    def handle(self, *args, **options):
        for track in self.tracks:
            Track.objects.get_or_create(
                major = Major.objects.get(title = track['major']),
                title = track['title'],
                student_year = StudentYear.objects.get(student_year=track['student_year'])
            )
        self.stdout.write(self.style.SUCCESS('Tracks initialized'))
        return 0
            
        