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
            
        