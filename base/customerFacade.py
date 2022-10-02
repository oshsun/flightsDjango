from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
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
from django.core.exceptions import ObjectDoesNotExist,ValidationError
from rest_framework.permissions import IsAuthenticated


@api_view(['PATCH'])
def update_customer(request,id):   ###  first checked
    if request.method =='PATCH':
        customer = Customer.objects.get(id=id)
        print(11111)
        print(customer)
        print(222222)
        if 'first_name' in request.data:
            customer.first_name=request.data['first_name']
        if 'last_name' in request.data:
            customer.last_name=request.data['last_name']
        if 'address' in request.data:
            customer.address=request.data['address']
        if 'phone_no' in request.data:
            customer.phone_no=request.data['phone_no']
        if 'credit_card_no' in request.data:
            customer.credit_card_no=request.data['credit_card_no']
        customer.save()
        serializer=CustomerSerializer(customer)
        return Response(data=serializer.data,status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def add_ticket(request):
    if request.method == 'POST':
        customer = Customer.objects.get(user=request.user)
        request.data['customer_id'] = customer.id
        serializer = TicketSerializer(data=request.data, many=False)
        if serializer.is_valid():
            ticket = serializer.save()
            flight = Flight.objects.get(id=request.data['flight_id'])
            flight.remaining_tickets -= 1
            flight.save()
            return Response(data=TicketSerializer(ticket).data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


@api_view(['DELETE'])  ###  first checked
def remove_ticket(request, id):
    if request.method == 'DELETE':
        print('before remove ticket')
        ticket = Ticket.objects.get(id=id)
        print(f'inside remove ticket, before adding back the ticket  {ticket.flight_id.remaining_tickets}')
        ticket.flight_id.remaining_tickets += 1
        print(f'inside remove ticket, before after back the ticket  {ticket.flight_id.remaining_tickets}')
        ticket.flight_id.save()
        ticket.delete()
        print('after remove ticket')

        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])  ###  first checked
def get_my_tickets(request):
    if request.method =='GET':
        customer_id= Customer.objects.get(id=request.data['customer_id'])
        tickets= customer_id.ticket_set.all()
        serializer = DisplayTicketSerializer(tickets, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
