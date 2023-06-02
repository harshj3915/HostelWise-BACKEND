import re
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Student

@api_view(['POST','GET'])
def STUDENTREGISTER(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.error_messages,status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        students=Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data,safe=False)  

'''@api_view(['POST'])
def GENERALLOGIN(request):
    if request.method=='POST':

'''