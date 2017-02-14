from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    #prerequisites - courses the student must pass before being able to take the course 
    #degree program restriction - course to be taken only by certain degree programs
    #year level restriction
    #alternatives - courses that can be taken in place of this course e.g. Math 11 and Math 14 is the same as taking Math 17
    #units

    def __unicode__(self):
        return self.name

class Offering(models.Model):
    DAY_CHOICES = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('Th', 'Thursday'),
        ('F', 'Friday'),
        ('S', 'Saturday')
    )

    course = models.ForeignKey(Course)
    start_time = models.TimeField()
    end_time = models.TimeField()
    section = models.PositiveIntegerField() 
    slots = models.PositiveIntegerField()
    #days = models.CharField(max_length=2, choices=DAY_CHOICES)
    #type - GE (AH, MST, SSP), Major, Elective, PE, NSTP
    #room
    #year level restriction
    #degree program restriction
    #instructor

#class OfferingEnlist(models.Model):
    #academicYear
    #semester
    #student
    #offering
    #dateEnlisted
    #status? enlisted, confirmed, enrolled?
