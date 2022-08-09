from email import message
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import re
from urllib import response
from django.http import HttpResponse
#from .users import users
#from .models import Users
from .models import *
from .serializers import *
from rest_framework import status
from django.db import transaction,IntegrityError
from rest_framework.parsers import JSONParser 

@api_view(['GET']) ###first checked
def get_all_customers(request):
    if request.method =='GET':
        customers =Customer.objects.all()
        serializer =CustomerSerializer(data=customers, many = True)
        serializer.is_valid()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


@api_view(['POST'])  ###first checked
def add_airline(request):
    if request.method =='POST':
        with transaction.atomic():
            user =User.objects.get(id=request.data['user_id'])
            if user.is_staff != 1:
                print(111)
                a= {"message": "this user is not airline"}
                print(a)
                return Response(status=status.HTTP_403_FORBIDDEN,data=a)
            else:
                new_airline = AirlineCompanySerializer(data=request.data)
                if new_airline.is_valid():
                    airline = new_airline.save()
                else:
                    return Response(new_airline.errors, status.HTTP_400_BAD_REQUEST)
                return Response(data=AirlineCompanySerializer(airline).data, status=status.HTTP_201_CREATED)

@api_view(['POST'])   ###first checked
def add_customer(request):
    if request.method =='POST':
        with transaction.atomic():
            user=User.objects.get(id=request.data['user_id'])
            print(user)
            new_customer = CustomerSerializer(instance=user, data=request.data)
            if new_customer.is_valid():
                customer = new_customer.save()
            else:
                return Response(new_customer.errors, status.HTTP_400_BAD_REQUEST)
            return Response(data=CustomerSerializer(customer).data, status=status.HTTP_201_CREATED)

@api_view(['POST'])   ###first checked
def add_administrator(request):
    if request.method =='POST':
        with transaction.atomic():
            user = User.objects.get(id=request.data['user_id'])
            if user.is_superuser != 1:
                print(111)
                a= 'this user is not admin'
                print(a)
                return Response(status.HTTP_403_FORBIDDEN)
            else:
                print(222)
                new_admin = AdminstratorSerializer(data=request.data)
                if new_admin.is_valid():
                    admin = new_admin.save()
                else:
                    return Response(new_admin.errors, status.HTTP_400_BAD_REQUEST)
                return Response(data=AdminstratorSerializer(admin).data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])   ###first checked
def remove_airline(request,id):
    if request.method =='DELETE':
        airline = AirlineCompany.objects.get(id=id)
        airline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])   ###first checked
def remove_customer(request,id):
    if request.method =='DELETE':
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])   ###first checked
def remove_administrator(request,id):
    if request.method =='DELETE':
        admin = Adminstrator.objects.get(id=id)
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)