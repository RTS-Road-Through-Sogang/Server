from django.core.management.base import BaseCommand
from Users.models import *
class Command(BaseCommand):
    help = 'Initialize StudentYear'
<<<<<<< HEAD
    StudentYear = [  
=======
    StudentYear = [
>>>>>>> 29977554764f97137138198ea7749a22d67f8411
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
            StudentYear.objects.get_or_create(
                student_year = studentyear['student_year'], 
                
            )
    
        
                        
        self.stdout.write(self.style.SUCCESS('Student year initialized'))
        return 0
            