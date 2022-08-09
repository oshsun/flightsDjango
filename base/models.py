from django.db import models
from email.message import EmailMessage
from email.policy import EmailPolicy
from tokenize import Name
from django.contrib.auth.models import User
from PIL import Image
import datetime

from base.validator import validate_phone_num

class Country(models.Model):
    #Id =models.AutoField(auto_created=True,primary_key=True,editable=False)
    name = models.CharField(max_length=32,unique=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')

    def __str__(self):
       return self.name

    class Meta:
        db_table ='countries'


class UserRole(models.Model):
    # CUSTOMER = 'CU'
    # AIRLINE_COMPANY = 'AC'
    # ADMIN = 'AD'
    # ROLE_NAME_CHOICES = [(CUSTOMER, 'Customer'),(AIRLINE_COMPANY, 'Airline Company'),(ADMIN, 'Admin')]
    # #Id =models.AutoField(auto_created=True,primary_key=True,editable=False)
    # Role_Name = models.CharField(max_length=2,choices=ROLE_NAME_CHOICES,default=CUSTOMER, unique=True)
    role_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
       return self.role_name


class MyUserProfile(models.Model):
    #Id =models.BigAutoField(auto_created=True ,primary_key=True,editable=False)
    #username = models.CharField(max_length=32,unique=True)
    #password = models.CharField(max_length=32)
    #email = models.EmailField(max_length=254,unique=True)
    user_id = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    user_role =  models.ForeignKey(UserRole, on_delete=models.SET_NULL,null=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    

    
    def __str__(self):
        return str(self.id)
       #return '{}/{}'.format(self.username,self.id)

 
class AirlineCompany(models.Model):
    #Id =models.BigAutoField(auto_created=True ,primary_key=True,editable=False)
    name = models.CharField(max_length=52,unique=True)
    country_id = models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    user_id = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
 
    class Meta:
        db_table ='airline_companies'
        
    def __str__(self):
       return self.name

    


class Flight(models.Model):
    #Id =models.BigAutoField(auto_created=True ,primary_key=True,editable=False)
    airline_company_id = models.ForeignKey(AirlineCompany,on_delete=models.SET_NULL,null=True)
    origin_country_id =models.ForeignKey(Country,on_delete=models.SET_NULL,null=True,related_name='origin_country_id')
    destination_country_id =models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    departure_time=models.DateTimeField()
    landing_time=models.DateTimeField()
    remaining_tickets=models.IntegerField()
 
    def __str__(self):
        return f'Flight from {str(self.origin_country_id)} to {str(self.destination_country_id)}'
      

class Customer(models.Model):
    #Id =models.BigAutoField(auto_created=True,primary_key=True,editable=False)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField( max_length=32)
    address = models.CharField( max_length=64)
    phone_no = models.CharField( max_length=32,unique=True)#,validators=[validate_phone_num])
    credit_card_no = models.CharField( max_length=64,unique=True)
    user_id =  models.OneToOneField(User,on_delete=models.SET_NULL,null=True)  
 
    def __str__(self):
       return self.first_name

class Ticket(models.Model):
    #Id =models.BigAutoField(auto_created=True,primary_key=True,editable=False)
    flight_id = models.ForeignKey(Flight,on_delete=models.SET_NULL,null=True)
    customer_id = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)

    class Meta:
        unique_together = ('flight_id', 'customer_id',)
        
    def __str__(self):
       return '{}/{}'.format(self.flight_id,self.customer_id)
    #        return '{}/{}'.format(self.flight_id,self.customer_id)

 

class Adminstrator(models.Model):
    #Id =models.AutoField(primary_key=True,editable=False)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    user_id =  models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    
    
    def __str__(self):
       return self.first_name
