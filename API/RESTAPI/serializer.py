from rest_framework import serializers
from .models import Student,Cleaner

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['s_SECRETKEY','s_Name','s_Gender','s_Email','s_password','s_Registration_Number','s_Room_Number','s_Block','date_added']
        