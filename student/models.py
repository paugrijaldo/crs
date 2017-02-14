from django.db import models
from django.contrib.auth.models import User

class DegreeProgram(models.Model):
    name = models.CharField(max_length=250) 
    description = models.TextField()
    #division

class Student(models.Model):
    SEX_CHOICES = (
        ('U', 'Undisclosed'),
        ('F', 'Female'),
        ('M', 'Male'),
    )

    student_number = models.ForeignKey(User)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    year_level = models.PositiveIntegerField(default=1)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='Undisclosed')
    date_of_birth = models.DateField() 
    degree_program = models.ForeignKey(DegreeProgram, default=None, null=True)
    #adviser
    #isSRV = models.BooleanField(default=False)
    #stfap bracket

    def __unicode__(self):
        return ' '.join([self.firstName, self.lastName])

    #def status(self, grades):
    #compute gwa here


#class StudyPlan(models.Model):
    #degree program
    #course
    #year
    #semester

#class EnrollmentData(models.Model):
    #academicYear
    #semester
    #student

#class Grade(models.Model):
    #academicYear
    #semester
    #student
    #course
    #grade

    #def status:
