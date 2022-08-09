from functools import partial
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
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

@api_view(['GET','POST','DELETE','PATCH'])
def customers(request,id=0):
    if request.method =='GET':
        try:
            if int(id) > 0: #get single customer
                customer = Customer.objects.get(id=id)
                serializer = CustomerSerializer(customer)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            else: #get all customers
                customers =Customer.objects.all()
                serializer =CustomerSerializer(data=customers, many = True)
                serializer.is_valid()
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Exception as ex:
            print (ex)
            return Response(status=status.HTTP_400_BAD_REQUEST)# data=ex)

    if request.method == 'POST':  # add a customer
        with transaction.atomic():
            user=User.objects.get(id=request.data['user_id'])
            print(user)
            new_customer = CustomerSerializer(instance=user, data=request.data)
            if new_customer.is_valid():
                customer = new_customer.save()
            else:
                return Response(new_customer.errors, status.HTTP_400_BAD_REQUEST)
            return Response(data=CustomerSerializer(customer).data, status=status.HTTP_201_CREATED)
                    
    if request.method =='DELETE': # delete a customer
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
    
    if request.method =='PATCH': # update a customer
        customer = Customer.objects.get(id=id)
        print(11111)
        print(customer)
        print(222222)
        if 'first_name'  in request.data:
            customer.first_name=request.data['first_name']
        if 'last_name'  in request.data:
            customer.last_name=request.data['last_name']
        if 'address'  in request.data:
            customer.address=request.data['address']
        if 'phone_no'  in request.data:
            customer.phone_no=request.data['phone_no']
        if 'credit_card_no'  in request.data:
            customer.credit_card_no=request.data['credit_card_no']
        customer.save()
        serializer=CustomerSerializer(customer)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
 


# @api_view(['GET','POST','DELETE','PATCH'])
# def myUsers(request,id=0):
#     if request.method =='GET':
#         try:
#             if int(id) > 0: #get single user
#                 user = User.objects.get(id=id)
#                 if user:
#                     serializer = UserSerializer(data=user)
#                     return Response(status=status.HTTP_200_OK, data=serializer.data)
#             else:
#                 users =User.objects.all() # get all users
#                 serializer =UserSerializer(data=users, many = True)
#                 print('test')
#                 if serializer.is_valid():  
#                     return Response(status=status.HTTP_200_OK, data=serializer.data)
#         except Exception as ex:
#             print (ex)
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=ex)

#     if request.method =='POST': # add user
#         with transaction.atomic():
#             serializer = UserSerializer(data=request.data)
#             if serializer.is_valid():
#                 try:
#                     serializer.save()
#                 except IntegrityError as ex:
#                     return  Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data=ex)
#                 return Response(status=status.HTTP_200_OK, data=serializer.data)
    
#     if request.method =='DELETE': # delete user
#         user = User.objects.get(id=id)
#         serializer = UserSerializer(data=user)
#         user.delete()
#         #return Response(status=status.HTTP_200_OK, data=serializer.data)
#         return JsonResponse({'DELETE': id})

#     if request.method =='PATCH': # update user
#         user = User.objects.get(id=id)
#         with transaction.atomic():
#             serializer = UserSerializer(data=request.data)
#             if serializer.is_valid():
#                 try:
#                     serializer.save()
#                 except IntegrityError as ex:
#                     return  Response(status=status.HTTP_405_METHOD_NOT_ALLOWED, data=ex)
#                 return Response(status=status.HTTP_200_OK, data=serializer.data)

