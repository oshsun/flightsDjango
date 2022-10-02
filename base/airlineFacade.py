from datetime import timezone

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializers import *
from rest_framework import status
from django.db import transaction

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_airline_company(request):
    if request.method == 'GET':
        user_id = request.user.id
        print('entered get')
        company = AirlineCompany.objects.get(user_id=user_id)
        print(f'entered got comapy ${company}')

        serializer = AirlineCompanySerializer(company, many=False)
        print(f'entered got seralizer worked  ${serializer}')

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_airline(request):
    if request.method == 'PUT':
        user_id = request.user.id
        airline = AirlineCompany.objects.get(user_id=user_id)
        country = Country.objects.get(name=request.data['country'])
        request.data['country_id'] = country.id
        serializer=UpdateAirlineCompanySerializer(airline, data=request.data)
        if serializer.is_valid():
            print('entered is valid')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# add to it later
# @permission_classes([IsAdminUser])

@api_view(['GET'])
def flight_detail(request, id):
    if request.method == 'GET':
        flight = Flight.objects.get(id=id)
        serializer = FlightSerializer(flight, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_flight_(request):
    if request.method == 'PUT':
        print(request.data)
        user_id = request.user.id
        flight = Flight.objects.get(id=request.data['flight_id'])
        airline_instance = AirlineCompany.objects.get(user_id=user_id)



        origin_country_id = Country.objects.get(name=request.data['origin_country'])
        request.data['origin_country_id'] = origin_country_id.id

        destination_country_id = Country.objects.get(name=request.data['destination_country'])
        request.data['destination_country_id'] = destination_country_id.id

        request.data['airline_company_id'] = airline_instance.id

        serializer = UpdateFlightSerializer(flight, data=request.data)
        if serializer.is_valid():
            print('entered is valid on update')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])  ### first checked
@permission_classes([IsAdminUser])
def add_flight(request):
    print('in add flight')
    if request.method == 'POST':
        with transaction.atomic():
            user_id = request.user.id
            airline_instance = AirlineCompany.objects.get(user_id=user_id)

            origin_country_id = Country.objects.get(name=request.data['origin_country'])
            request.data['origin_country_id'] = origin_country_id.id
            destination_country_id = Country.objects.get(name=request.data['destination_country'])
            request.data['destination_country_id'] = destination_country_id.id
            request.data['airline_company_id'] = airline_instance.id

            if request.data['departure_time'] > request.data['landing_time']:
                print('landing_time must be bigger than departure time')
                return Response(status.HTTP_400_BAD_REQUEST)

            # if request.data['destination_country_id'] == request.data['airline_company_id']:
            if request.data['destination_country_id'] == request.data['origin_country_id']:
                return Response(status.HTTP_400_BAD_REQUEST)

            serializer = AddFlightSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])  ### first checked
def update_flight(request,id):
    if request.method == 'PATCH':
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
@permission_classes([IsAuthenticated])
def remove_flight(request,id):
    if request.method =='DELETE':
        print('before remove flight')
        flight = Flight.objects.get(id=id)
        print('after remove')

        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_my_flights(request):  ### first checked
    if request.method == 'GET':
        airline = AirlineCompany.objects.get(user_id=request.user.id)
        flights = airline.flight_set.all()
        print(flights)
        serializer = FlightSerializer(flights, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

