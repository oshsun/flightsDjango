from django.db import models

from base.validator import *


class Country(models.Model):
    name = models.CharField(max_length=32,unique=True)
    image_url = models.URLField()

    def __str__(self):
       return self.name

    class Meta:
        db_table ='countries'


class UserRole(models.Model):
    role_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
       return self.role_name


class MyUserProfile(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    user_role =  models.ForeignKey(UserRole, on_delete=models.SET_NULL,null=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')

    def __str__(self):
        return str(self.id)

 
class AirlineCompany(models.Model):
    name = models.CharField(max_length=52,unique=True)
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL,null=True)
    user_id = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
 
    class Meta:
        db_table ='airline_companies'
        
    def __str__(self):
       return self.name


class Flight(models.Model):
    airline_company_id = models.ForeignKey(AirlineCompany,on_delete=models.SET_NULL,null=True)
    origin_country_id =models.ForeignKey(Country,on_delete=models.CASCADE, related_name='origin_country_id')
    destination_country_id =models.ForeignKey(Country,on_delete=models.CASCADE)
    departure_time=models.DateTimeField()
    landing_time=models.DateTimeField()
    remaining_tickets=models.IntegerField(validators=[validate_flight_tickets])

    def __str__(self):
        return f'Flight from {str(self.origin_country_id)} to {str(self.destination_country_id)}'


class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    phone_no = models.CharField(max_length=32, unique=True, validators=[validate_phone_num])
    credit_card_no = models.CharField(max_length=64, unique=True, validators=[validate_credit_card])
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Ticket(models.Model):
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('flight_id', 'customer_id',)


class Adminstrator(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    user_id =  models.OneToOneField(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
       return self.first_name
