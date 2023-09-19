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
            'category23': '전공입문교과',
            'category22': '전공입문교과',
            'category21': '전공입문교과',
            'category20': '전공입문교과',
            'category19': '전공입문교과'
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
            'category20': '전공입문교과',
            'category19': '전공입문교과'
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
            'category20': '전공입문교과',
            'category19': '전공입문교과'
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
            'category20': '전공입문교과',
            'category19': '전공입문교과'
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
            'category20': '전공입문교과',
            'category19': '전공입문교과'
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
            'category20': '전공입문교과',
            'category19': '전공입문교과'
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
            'category20': '전공입문교과',
            'category19': '전공입문교과'
        },
        {   'title': '응용수학1',
            'code':'MAT2010',
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
            'category20': '전공입문교과',
            'category19': '전공입문교과'
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
            
        