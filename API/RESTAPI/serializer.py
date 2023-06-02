from rest_framework import serializers

from .models import Student, Cleaner, SuperUser


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('s_SECRETKEY', 's_Name', 's_Gender', 's_Email', 's_Password', 's_Registration_Number', 's_Room_Number', 's_Block', 's_Type', 'date_added')


class CleanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaner
        fields = ('c_Name', 'c_Gender', 'c_Phone', 'c_Password', 'c_Registration_Number', 'c_Block', 's_Type', 'date_added')


class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperUser
        fields = ('su_ID', 'su_Password', 'su_Name', 'su_Block', 's_Type', 'date_added')
