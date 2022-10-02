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

    def save(self):
        user = User(email=self.validated_data['email'],
                    username=self.validated_data['username'],
                    is_staff=self.validated_data['is_staff'],
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



class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'


class MyUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUserProfile
        fields = ['user_role','user_id']


class AirlineCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirlineCompany
        fields = '__all__'
        depth = 1


class UpdateAirlineCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirlineCompany
        fields = ['name', 'country_id']


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        depth = 1


class AddFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class UpdateFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['origin_country_id', 'destination_country_id', 'departure_time', 'landing_time', 'remaining_tickets']



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class DisplayTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        depth=2


class AdminstratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adminstrator
        fields = '__all__'

    # def save(self,*args,**kwarg):
    #     admin = Adminstrator(first_name=self.validated_data['first_name'],
    #     last_name=self.validated_data['last_name'],
    #     user_id=self.validated_data['user_id']
    #
    #     )
    #     admin.save()
    #     return admin
