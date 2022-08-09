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
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist,ValidationError

def about(req):
    return HttpResponse('<h1>about first</h1>')


@api_view(['GET'])
def get_airline_by_username(request):  ### first checked
    if request.method =='GET':
        try:
            user = User.objects.get(username=request.data['username'])
            airline = AirlineCompany.objects.get(user_id=user.id)
            serializer = AirlineCompanySerializer(airline)
            #serializer.is_valid()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except ObjectDoesNotExist as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data="there is no airline for the written username")

@api_view(['GET'])  ### first checked
def get_customer_by_username(request):
    if request.method =='GET':
        try:
            user = User.objects.get(username=request.data['username'])
            customer = Customer.objects.get(user_id=user.id)
            print(customer)
            if customer:
                serializer = CustomerSerializer(customer)
                print(customer)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            else:
                message="there is no customer for the written username "
                return Response(status=status.HTTP_400_BAD_REQUEST,data =message)
        except ObjectDoesNotExist as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data="there is no customer for the written username")


@api_view(['GET'])  ### first checked
def get_user_by_username(request):  
    if request.method =='GET':
        try:
            user = User.objects.get(username=request.data['username'])
            serializer = UserSerializer(user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except ObjectDoesNotExist as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data="there is no user for the written username")

@api_view(['POST'])  ### first checked
def get_flights_by_parameters(request):
    if request.method =='POST':
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(request.data)
        try:
            flights = Flight.objects.filter(origin_country_id=request.data['origin_country_id']).filter(destination_country_id=request.data['destination_country_id']).filter(departure_time=request.data['date'])
            serializer = FlightSerializer(data=flights,many=True)
            serializer.is_valid()
            if len(flights) ==0:
                message ='there is no matching flight'   
                return Response(status=status.HTTP_400_BAD_REQUEST,data=message)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except ValidationError as ex:
             return Response(status=status.HTTP_400_BAD_REQUEST,data="date value must be in YYYY-MM-DD format")
        except ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data="origin_country_id field and destination_country_id field must be number")


@api_view(['GET'])  ### first checked
def get_flights_by_airline_id(request):
    if request.method =='GET':
        try: 
            flights = Flight.objects.filter(airline_company_id=request.data['airline_company_id'])
            serializer = FlightSerializer(data=flights,many=True)
            serializer.is_valid()
            if len(flights) ==0:
                message ='there are no flights of the chosen airline company'   
                return Response(status=status.HTTP_400_BAD_REQUEST,data=message)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data="airline_company_id field and must be number")


@api_view(['GET'])  ### first checked
def get_arrival_flights(request):
    if request.method =='GET':
        try:
            now =datetime.now()
            later =now+timedelta(hours = 12)
            flights=Flight.objects.filter(destination_country_id=request.data['destination_country_id']).filter(landing_time__gte=now ).filter(landing_time__lte=later)
            serializer = FlightSerializer(data=flights,many=True)
            serializer.is_valid()
            if len(flights) ==0:
                message ='there are no upcoming flights for the next 12 hours'   
                return Response(status=status.HTTP_400_BAD_REQUEST,data=message)
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        except ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data="destination_country_id field and must be number")

@api_view(['GET'])   ### first checked
def get_departure_flights(request):
    if request.method =='GET':
        try:
            now =datetime.now()
            later =now+timedelta(hours = 12)
            flights=Flight.objects.filter(origin_country_id=request.data['origin_country_id']).filter(departure_time__gte=now ).filter(departure_time__lte=later)
            serializer = FlightSerializer(data=flights,many=True)
            serializer.is_valid()
            if len(flights) ==0:
                message ='there are no flights for the next 12 hours'   
                return Response(status=status.HTTP_400_BAD_REQUEST,data=message)
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        except ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data="origin_country_id field and must be number")

@api_view(['GET'])  ### first checked
def get_tickets_by_customer(request):
    if request.method =='GET':
        try:
            customer_id= Customer.objects.get(id=request.data['customer_id'])
            tickets= customer_id.ticket_set.all()
            serializer = TicketSerializer(tickets,many=True)
            if len(tickets) ==0:
                message ='there are no tickets for the customer'   
                return Response(status=status.HTTP_400_BAD_REQUEST,data=message)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data="customer_id field must be number")
        except ObjectDoesNotExist as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data="there is no such customer")


@api_view(['POST'])  ### first checked
def get_flights_by_country(request):
    if request.method =='POST':
        try:
            flights = Flight.objects.filter(destination_country_id=request.data['destination_country_id'])
            serializer = FlightSerializer(data=flights,many=True)
            serializer.is_valid()
            if len(flights) ==0:
                message ='there is no matching flight'   
                return Response(status=status.HTTP_400_BAD_REQUEST,data=message)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        # except ValidationError as ex:
        #      return Response(status=status.HTTP_400_BAD_REQUEST,data="date value must be in YYYY-MM-DD format")
        except ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data="origin_country_id field and destination_country_id field must be number")


    



def index(req):
    return JsonResponse('hello', safe=False)



 
