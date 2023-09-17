from django.core.management.base import BaseCommand
from Users.models import *
class Command(BaseCommand):
    help = 'Initialize StudentYear'
    StudentYear = [  
        {
            'student_year': 19,
            
        }, 
        {
            'student_year': 20,
            
        }, 
        {
            'student_year': 21,
            
        }, 
        {
            'student_year': 22,
            
        }, 
        {
            'student_year': 23,
            
        }, 
        {
            'student_year': 24,
            
        }, 

    ]
    

    def handle(self, *args, **options):
        for studentyear in self.StudentYear:
            Major.objects.get_or_create(
                studentyear = studentyear['student_year'], 
                
            )
       
        
                        
        self.stdout.write(self.style.SUCCESS('Student year initialized'))
        return 0
            