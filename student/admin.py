from django.contrib import admin
from student.models import *
from django.http import HttpResponse
from django.conf.urls import patterns

class StudentAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'student_number')


admin.site.register(Student, StudentAdmin)
admin.site.register(DegreeProgram)
