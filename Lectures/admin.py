from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(CategoryDetail)
admin.site.register(Tech)
admin.site.register(Subject)

admin.site.register(TechInSubject)
admin.site.register(Route)
admin.site.register(SubjectInRoute)