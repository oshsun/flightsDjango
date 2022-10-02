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
from django.core.serializers import serialize 
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import ObjectDoesNotExist,ValidationError

### === firsrt checked

@api_view(['GET'])  ### firsrt checked
def get_all_flights(request):
    if request.method =='GET':
        flights=Flight.objects.all()
        serializer =FlightSerializer(data=flights, many = True)
        serializer.is_valid()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


@api_view(['GET'])   ### firsrt checked
def get_flight_by_id(request,id):
    if request.method =='GET':
        try:
            if int(id) > 0: #get single customer
                flight = Flight.objects.get(id=id)
                serializer = FlightSerializer(flight)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        except ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data='flight id must be number')
        except ObjectDoesNotExist as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data='there is no matching flight')
        except AssertionError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data='there is no matching flight')


@api_view(['GET'])   ### firsrt checked
def get_flights_by_parameters(request): #(origin_country_id,  destination_country_id,   date)
    if request.method =='GET':
        try:
            flights = Flight.objects.filter(origin_country_id=request.data['origin_country_id']).filter(destination_country_id=request.data['destination_country_id']).filter(departure_time=request.data['date'])
            serializer = FlightSerializer(data=flights,many=True)
            serializer.is_valid()
            if len(flights) ==0:
                message ='there is no matching flight'     # לבדוק מה אם אין טיסה
                return Response(status=status.HTTP_400_BAD_REQUEST,data=message)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except ValidationError as ex:
             return Response(status=status.HTTP_400_BAD_REQUEST,data="date value must be in YYYY-MM-DD format")
        except ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data="origin_country_id field and destination_country_id field must be number")
        

@api_view(['GET'])   ### firsrt checked
def get_all_airlines(request):
    if request.method =='GET':
        airlines=AirlineCompany.objects.all()
        serializer =AirlineCompanySerializer(data=airlines, many = True)
        serializer.is_valid()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
        

@api_view(['GET'])    ### firsrt checked
def get_airline_by_id(request,id):
    if request.method =='GET':
        try:
            if int(id) > 0: 
                airline = AirlineCompany.objects.get(id=id)
                serializer = AirlineCompanySerializer(airline)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        except AssertionError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data='there is no matching airline')
        except ObjectDoesNotExist as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data='there is no matching airline')
        except ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data='airline id must be number')

@api_view(['GET'])   ### firsrt checked 
def get_airline_by_parameters(request):  
    if request.method =='GET':
        try:
            airlines = AirlineCompany.objects.filter(country_id = request.data['country_id'])
            serializer = AirlineCompanySerializer(data=airlines, many=True)
            serializer.is_valid()
            if len(airlines) ==0:
                message ='there is no matching airline'   
                return Response(status=status.HTTP_400_BAD_REQUEST,data=message)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data='country id must be number') 

@api_view(['GET'])  ### firsrt checked 
def get_all_countries(request):
    if request.method =='GET':
        countries=Country.objects.all()
        serializer =CountrySerializer(data=countries, many = True)
        serializer.is_valid()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
        
        

@api_view(['GET'])   ### firsrt checked 
def get_country_by_id(request,id):
    if request.method =='GET':
        try:
            if int(id) > 0: 
                country = Country.objects.get(id=id)
                serializer = CountrySerializer(country)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        except ValueError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data='country id must be number')
        except ObjectDoesNotExist as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data='there is no matching country')
        except AssertionError as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST,data='there is no matching country')

# add new user / register / sign up
@api_view(['POST'])  ### firsrt checked 
def create_new_user(request):
    if request.method =='POST':
            print(request.data)
            if request.data['is_superuser'] == 'true':
                request.data['is_staff'] = 'true'
            serializer=UserSerializer(data=request.data)
            if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED, data=serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)