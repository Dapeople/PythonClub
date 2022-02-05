from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#
#
#Meeting which will have fields for meeting title, 
# meeting date, meeting time, location, Agenda
#
class Meeting(models.Model):
    MeetingTitle=models.TextField()
    MeetingDate=models.DateField()
    MeetingTime=models.TimeField()
    MeetingID=models.PositiveIntegerField()
    Location=models.TextField()
    Agenda=models.TextField()

    def __str__(self):
        return self.MeetingTitle()

    class Meta:
        db_table='Meeting'
        verbose_name_plural='Meetings'


#Meeting Minutes which will have fields for meeting id (a foreign key), 
# attendance (a many to many field with User), Minutes text
class MeetingMinutes(models.Model):
    MeetingID=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    Attendance=models.ManyToManyField(User) #RESOLVE MANY TO MANY RELATIONSHIP
    MinutesText=models.TextField()


    def __str__(self):
        return self.MeetingID()

    class Meta:
        db_table='MeetingMinutes'
#
#Resource which will have fields for resource name, resource type, 
# URL, date entered, user id (foreign key with User), and description
#
class Resource(models.Model):
#
    ResourceName=models.TextField
    ResourceType=models.TextField
    URL=models.URLField()
    DateEntered=models.DateField()
    UserID=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    Description=models.TextField()

    def __str__(self):
        return self.ResourceName()

    class Meta:
        db_table='Resource'
        verbose_name_plural='Resources'
#
#
#Event which will have fields for event title, location, date, 
# time, description and the user id of the member that posted it
class Event(models.Model):
    Title=models.TextField()
    Location=models.TextField()
    Date=models.DateField()
    Time=models.TimeField()
    Description=models.TextField()
    UserID=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Title()

    class Meta:
        db_table='Event'
        verbose_name_plural='Events'

#Created this one expecting that it is needed. Might need more details later
class User(models.Model):
    UserName=models.TextField()
    UserID=models.PositiveIntegerField()

    def __str__(self):
        return self.UserName()

    class Meta:
        db_table='User'
        verbose_name_plural='Users'

# Probably not needed, keeping in case it is
# class MinutesToUser(models.Model):
#    UserID=models.ForeignKey(User, on_delete=models.CASCADE)
#    Attendance=models.ForeignKey(MeetingMinutes, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.()
#    
#    class Meta:
#        db_table=''
#