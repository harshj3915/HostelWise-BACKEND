import re
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .serializer import RoomCleanDataSerializer, StudentSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Student,Cleaner,SuperUser,RoomCleanData
import json

#ngrok http 8000

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
    if request.method == 'POST':
        login_data = request.data.get('LOGIN')
        password_data = request.data.get('PASSWORD')

        user1 = Student.objects.filter(s_Email=login_data, s_Password=password_data).first()
        user2 = Cleaner.objects.filter(c_Registration_Number=login_data, c_Password=password_data).first()
        user3 = SuperUser.objects.filter(su_ID=login_data, su_Password=password_data).first()
        user = None

        if user1 is not None:
            user = model_to_dict(user1)
            sk =  user['s_SECRETKEY']
            t= user['s_Type']
            
        elif user2 is not None:
            user = model_to_dict(user2)
            sk =  user['c_SECRETKEY']
            t= user['c_Type']
            
        elif user3 is not None:
            user = model_to_dict(user3)
            sk =  user['su_SECRETKEY']
            t= user['su_Type']
            

        if user is not None:
            sk1 = {"SECRETKEY":sk, "TYPE":t}
            return Response(sk1, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST'])
def GENERALDASHBOARD(request,api_key,action):
    
    if Student.objects.filter(s_SECRETKEY = api_key).exists:
        CURRENT_STUDENT=Student.objects.get(s_SECRETKEY = api_key)
        if request.method == 'POST':
            #Room cleaning --> action = A
            if action=="A":
                if CURRENT_STUDENT.s_Already_Requested_Room_clean==True:
                    return Response(status=status.HTTP_208_ALREADY_REPORTED)
                else:
                    serializer = RoomCleanDataSerializer(data={'student': CURRENT_STUDENT.pk})
                    CURRENT_STUDENT.s_Already_Requested_Room_clean=True
                    CURRENT_STUDENT.save()
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
                
                return Response(status=status.HTTP_200_OK)


            #Register complain --> action = B
            elif action == "B":
                return Response(status=status.HTTP_200_OK)


            #Maintainance request --> action = C
            elif action == "C":
                return Response(status=status.HTTP_200_OK)


            #Request mess food --> action = D
            elif action == "D":
                return Response(status=status.HTTP_200_OK)
        

        elif request.method=='GET':
            
            if action == 'Z':
                print('us')
                user = model_to_dict(CURRENT_STUDENT)
                del user['s_SECRETKEY']
                del user['s_Password']
                print(user)
                return Response(user, status=status.HTTP_202_ACCEPTED)



        


