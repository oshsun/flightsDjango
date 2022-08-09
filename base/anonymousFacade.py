from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
import re
from urllib import response
from django.http import HttpResponse
#from .users import users
#from .models import Users
from .models import User,Customer,UserRole
from .serializers import UserRoleSerializer,CustomerSerializer
from rest_framework import status
from django.db import transaction,IntegrityError
from rest_framework.parsers import JSONParser 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        # ...
 
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])  ### first checked  # 
def add_customer(request):    # יש לבדוק לגבי הוספת אשראי או טלפון עם אותיות
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

