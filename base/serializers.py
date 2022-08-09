from urllib import request
from django.http import JsonResponse
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'username',
            'is_staff',
            'is_superuser'
        )

        extra_kwargs = {'password':{'write_only':True}}
        depth = 0

    def save(self):
        # is_staff_flag =False
        # is_superuser_flag =False
        # if self.validated_data['role'] == 'Admin':
        #     is_staff_flag= True
        # if self.validated_data['role'] == 'Airline-Company':
        #     is_superuser_flag= True
            
        user = User(email=self.validated_data['email'],
                    username=self.validated_data['username'],
                    is_staff=self.validated_data['is_staff'],
                    # is_superuser=is_superuser_flag
                    is_superuser=self.validated_data['is_superuser'],
                    
                    )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

    def save(self):
        country = Country(name=self.validated_data['name']             
        )
        country.save()
        return country

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

    def save(self):
        role = UserRole(role_name=self.validated_data['role_name']             
        )
        role.save()
        return role

class MyUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUserProfile
        fields = ['user_role','user_id']
    def save(self):
        myprofile = MyUserProfile(username=self.validated_data['username'],
                                user_id=self.instance
               
        )
        myprofile.save()
        return myprofile

class AirlineCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirlineCompany
        fields = '__all__'

    def save(self,*args,**kwarg):
        company = AirlineCompany(name=self.validated_data['name'],
        country_id=self.validated_data['country_id'], 
        user_id=self.validated_data['user_id'] 
                     
        )
        company.save()
        return company

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def save(self,*args,**kwarg):
        flight = Flight(airline_company_id=self.validated_data['airline_company_id'],
        origin_country_id=self.validated_data['origin_country_id'], 
        destination_country_id=self.validated_data['destination_country_id'] ,
        departure_time=self.validated_data['departure_time'],
        landing_time=self.validated_data['landing_time'],
        remaining_tickets=self.validated_data['remaining_tickets']      
        )
        flight.save()
        return flight


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

        # extra_kwargs = {'credit_card_no':{'write_only':True}}
        depth = 1

    def save(self):
        customer = Customer(first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
                    address=self.validated_data['address'],
                    phone_no=self.validated_data['phone_no'],
                    credit_card_no=self.validated_data['credit_card_no'],
                    user_id=self.instance             
        )
        customer.save()
        return customer
 
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

    def save(self,*args,**kwarg):
        ticket = Ticket(flight_id=self.validated_data['flight_id'],
        customer_id=self.validated_data['customer_id']           
        )
        ticket.save()
        return ticket

class AdminstratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adminstrator
        fields = '__all__'

    def save(self,*args,**kwarg):
        admin = Adminstrator(first_name=self.validated_data['first_name'], 
        last_name=self.validated_data['last_name'], 
        user_id=self.validated_data['user_id'] 
                     
        )
        admin.save()
        return admin
