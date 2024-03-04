from django.db import models

# Create your models here.
class Mentor(models.Model):
    MentorID = models.CharField(max_length = 5 , primary_key = True)
    MentorName = models.CharField(max_length = 50)
    MentorPhoneNumber = models.CharField(max_length = 12)
    MentorDepartment = models.CharField(max_length = 20)
    MentorRoomNo = models.CharField(max_length = 5)
    Password = models.TextField(default = "123456789")


class Student(models.Model):
    StudentID = models.CharField(max_length = 11 , primary_key = True)
    StudentName = models.CharField(max_length = 50 )
    StudentCourse = models.CharField(max_length = 50)
    StudentClass = models.CharField(max_length = 10)
    StudentPhoneNumber = models.CharField(max_length = 12)
    MentorID = models.ForeignKey(Mentor, on_delete = models.CASCADE)
    Password = models.TextField(default = "123456789")

class Adminstration(models.Model):
    AdminId = models.CharField(max_length = 5 , primary_key = True)
    AdminName = models.CharField(max_length = 50)
    AdminPhoneNo = models.CharField(max_length = 12)
    Password = models.TextField(default = "123456789")

class AbsentReason(models.Model):
    MentorID = models.ForeignKey(Mentor , on_delete= models.CASCADE)
    StudentID = models.ForeignKey(Student , on_delete = models.CASCADE)
    Reason = models.CharField(max_length=100)
    Date = models.DateField()
    Status = models.CharField(max_length = 10 , default="Pending" )
    

    


    
