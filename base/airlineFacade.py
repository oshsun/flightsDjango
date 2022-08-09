
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


@api_view(['PATCH'])  ### first checked
def update_airline(request,id):
    if request.method =='PATCH':
        airline = AirlineCompany.objects.get(id=id)
        print(11111)
        print(airline)
        print(222222)
        if 'name'in request.data:
            airline.name=request.data['name']
        if 'country_id'in request.data:
            airline.country_id=request.data['country_id']
        airline.save()
        serializer=AirlineCompanySerializer(airline)
        return Response(data=serializer.data,status=status.HTTP_200_OK)




@api_view(['POST'])  ### first checked
def add_flight(request):
    if request.method =='POST':
        with transaction.atomic():
            new_flight = FlightSerializer(data=request.data)
            if new_flight.is_valid():
                flight = new_flight.save()
            else:
                return Response(new_flight.errors, status.HTTP_400_BAD_REQUEST)
            return Response(data=FlightSerializer(flight).data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])  ### first checked
def update_flight(request,id):
    if request.method =='PATCH':
        flight = Flight.objects.get(id=id)
        print(11111)
        print(flight)
        print(222222)
        #flight.airline_company_id=request.data['airline_company_id']
        if 'origin_country_id'in request.data:
            origin_country_id = Country.objects.get(id=request.data['origin_country_id'])
            flight.origin_country_id=origin_country_id
        if 'destination_country_id'in request.data:
            destination_country_id = Country.objects.get(id=request.data['destination_country_id'])
            flight.destination_country_id=destination_country_id
        if 'departure_time'in request.data:
            flight.departure_time=request.data['departure_time']
        if 'landing_time'in request.data:
            flight.landing_time=request.data['landing_time']
        if 'remaining_tickets'in request.data:
            flight.remaining_tickets=request.data['remaining_tickets']
        flight.save()
        serializer=FlightSerializer(flight)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['DELETE'])  ### first checked
def remove_flight(request,id):
    if request.method =='DELETE':
        flight = Flight.objects.get(id=id)
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_my_flights(request):  ### first checked
    if request.method =='GET':
        airline = AirlineCompany.objects.get(id=request.data['airline_company_id'])
        print(airline)
        flights = airline.flight_set.all()
        print(flights)
        serializer =FlightSerializer(flights, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

