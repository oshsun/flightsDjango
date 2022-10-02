from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customer_profile(request):
    print('i have been called')
    print(request.user)
    try:
        customer = Customer.objects.get(user_id=request.user.id)
        print(customer)
        serializer = CustomerSerializer(customer, many=False)
    except:
        return Response(False)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def place_customer(request):
    user = request.user.id
    request.data['user'] = user
    if request.method == 'POST':
        print(f'line 98 {request.data}')
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('saved!')
            return Response(serializer.data, status=HTTP_201_CREATED)
        print(f'serialzier erros print {serializer.errors}')
        print(serializer.errors)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        customer = Customer.objects.get(user=request.user)
        if request.data['first_name'] == "":
            request.data['first_name'] = customer.first_name
        if request.data['last_name'] == "":
            request.data['last_name'] = customer.last_name
        if request.data['phone_no'] == "":
            request.data['phone_no'] = customer.phone_no
        if request.data['address'] == "":
            request.data['address'] = customer.address
        if request.data['credit_card_no'] == "":
            request.data['credit_card_no'] = customer.credit_card_no
        print('line 118')
        serializer = CustomerSerializer(customer, data=request.data)
        print('line 120')
        print(request.data)
        if serializer.is_valid():
            print('line 123')
            serializer.save()
            print('line 126')
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


