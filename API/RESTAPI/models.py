from enum import auto
from django.db import models
class Student(models.Model):
    s_SECRETKEY = models.AutoField(primary_key=True)
    s_Name = models.CharField(max_length=100)
    s_Gender = models.CharField(max_length=10)
    s_Email = models.CharField(max_length=100,unique=True)
    s_Password = models.CharField(max_length=100)
    s_Registration_Number = models.CharField(max_length=10, unique=True)
    s_Room_Number = models.CharField(max_length=10)
    s_Block = models.CharField(max_length=1)
    s_Type = models.CharField(max_length=10,default='STUDENT')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.s_Name} : {self.s_Registration_Number}'
    
class Cleaner(models.Model):
    c_Name = models.CharField(max_length=100)
    c_Gender = models.CharField(max_length=10)
    c_Phone = models.CharField(max_length=10,unique=True)
    c_Password = models.CharField(max_length=100,default='defaultpw')
    c_Registration_Number = models.CharField(max_length=10, unique=True, primary_key=True)
    c_Block = models.CharField(max_length=1)
    c_Type = models.CharField(max_length=10,default='CLEANER')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.c_Name} : {self.c_Block}'
    
class SuperUser(models.Model):
    su_ID=models.CharField(max_length=100,primary_key=True,unique=True)
    su_Password=models.CharField(max_length=100)
    su_Name=models.CharField(max_length=100)
    su_Block=models.CharField(max_length=10)
    su_Type = models.CharField(max_length=10,default='SUPERUSER')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.su_Name} : {self.su_ID}'



