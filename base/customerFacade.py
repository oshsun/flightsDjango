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
from django.core.exceptions import ObjectDoesNotExist,ValidationError


@api_view(['PATCH'])
def update_customer(request,id):   ###  first checked
    if request.method =='PATCH':
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

@api_view(['POST'])  ###  first checked
def add_ticket(request):
    if request.method =='POST':
        with transaction.atomic():
            try:
                customer=Customer.objects.get(id=request.data['customer_id'])
                flight=Flight.objects.get(id=request.data['flight_id'])
                print(customer,flight)
                new_ticket = TicketSerializer(data=request.data)
                if new_ticket.is_valid():
                    ticket = new_ticket.save()
                else:
                    return Response(new_ticket.errors, status.HTTP_400_BAD_REQUEST)
                return Response(data=TicketSerializer(ticket).data, status=status.HTTP_201_CREATED)
            except ObjectDoesNotExist as ex:
                return Response(status=status.HTTP_400_BAD_REQUEST,data="customer or flight does not exist")
            except ValueError as ex:
                return Response(status=status.HTTP_400_BAD_REQUEST,data="customer_id field and flight_id must be number")
        return Response (tatus=status.HTTP_400_BAD_REQUEST, data="something went wrong")

@api_view(['DELETE'])  ###  first checked
def remove_ticket(request,id):
    if request.method =='DELETE':
        ticket = Ticket.objects.get(id=id)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])  ###  first checked
def get_my_tickets(request):
    if request.method =='GET':
        customer_id= Customer.objects.get(id=request.data['customer_id'])
        tickets= customer_id.ticket_set.all()
        serializer = TicketSerializer(tickets,many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
