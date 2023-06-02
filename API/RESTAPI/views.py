import re
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Student,Cleaner,SuperUser
import json

@api_view(['POST','GET'])
def STUDENTREGISTER(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data.copy()
            del serialized_data['s_Password']
            return Response(data=serialized_data,status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.error_messages,status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        students=Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data,safe=False)
    

@api_view(['POST'])
def GENERALLOGIN(request):
    if request.method=='POST':
        user1 = Student.objects.filter(s_Email=request.data['LOGIN'],s_Password=request.data['PASSWORD'])
        user2 = Cleaner.objects.filter(c_Registration_Number=request.data['LOGIN'],c_Password=request.data['PASSWORD'])
        user3 = SuperUser.objects.filter(su_ID=request.data['LOGIN'],su_Password=request.data['PASSWORD'])
        user=None
        if user1!=None:
            user=user1[0]
            user=model_to_dict(user)
            del user['s_Password']
            return Response(user,status=status.HTTP_202_ACCEPTED)
        elif user2!=None:
            user=user2[0]
            user=model_to_dict(user)
            del user['c_Password']
            return Response(user,status=status.HTTP_202_ACCEPTED)
        elif user3!=None:
            user=user3[0]
            user=model_to_dict(user)
            del user['su_Password']
            return Response(user,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

