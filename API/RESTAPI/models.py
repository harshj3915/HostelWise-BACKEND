from enum import auto
from django.db import models
class Student(models.Model):
    s_SECRETKEY = models.AutoField(primary_key=True)
    s_Name = models.CharField(max_length=100)
    s_Gender = models.CharField(max_length=10)
    s_Email = models.CharField(max_length=100,unique=True)
    s_password = models.CharField(max_length=15)
    s_Registration_Number = models.CharField(max_length=10, unique=True)
    s_Room_Number = models.CharField(max_length=10)
    s_Block = models.CharField(max_length=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.s_Name} : {self.s_Registration_Number}'
    
class Cleaner(models.Model):
    c_Name = models.CharField(max_length=100)
    c_Gender = models.CharField(max_length=10)
    c_Phone = models.CharField(max_length=10,unique=True)
    c_Registration_Number = models.CharField(max_length=10, unique=True, primary_key=True)
    c_Block = models.CharField(max_length=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.c_Name} : {self.c_Block}'
    



