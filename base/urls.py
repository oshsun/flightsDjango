"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from base import anonymousFacade, facadeBase, airlineFacade,customerFacade,administratorFacade
from . import views, customersView
from rest_framework_simplejwt.views import TokenObtainPairView
from .anonymousFacade import MyTokenObtainPairView
 
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



urlpatterns = [
    path('', views.index),
    path('getairlinebyusername', views.get_airline_by_username),
    path('getcustomerbyusername', views.get_customer_by_username),
    path('getuserbyusername', views.get_user_by_username),
    path('getflightsbyparam', views.get_flights_by_parameters),
    path('getflightsbyairlineid', views.get_flights_by_airline_id),
    path('getarrivalflights', views.get_arrival_flights),
    path('getdepartureflights', views.get_departure_flights),

    path('getticketsbycustomer', views.get_tickets_by_customer),


    path('getflightsbycountry', views.get_flights_by_country),

    
    #path('customers/<username>', customersView.customers),

    
    #path('customers', customersView.customers),
    #path('customers/<id>', customersView.customers),


    # facadeBase URLS
    path('flights', facadeBase.get_all_flights),
    path('flights/<id>', facadeBase.get_flight_by_id),
    path('flightsbyparameters', facadeBase.get_flights_by_parameters),
    path('airlines', facadeBase.get_all_airlines),
    path('airlines/<id>', facadeBase.get_airline_by_id),#get_airline_by_id
    path('airlinesbyparameters', facadeBase.get_airline_by_parameters),#get_airline_by_parameters
    path('countries', facadeBase.get_all_countries),#get_all_countries
    path('countries/<id>', facadeBase.get_country_by_id),#get_country_by_id
    path('adduser', facadeBase.create_new_user),#create_new_user

    #new flights by param function
    path('flight-by-params/', views.flight_by_params),  # get_country_by_id
    # path('flight-by-params/<str:origin_name>/<str:dest_name>/<str:dept_date>/', views.flight_by_params),  # get_country_by_id



    # anonymousFacade URLS
    # login
    path('addcustomer/', anonymousFacade.add_customer), #add_customer
    path('getflightsbycountry', views.get_flights_by_country),

    # airlineFacade URLS
    path('get_airline_company/', airlineFacade.get_airline_company),
    path('update-airline/', airlineFacade.update_airline),
    path('add-flight/', airlineFacade.add_flight),




    # path('updateflight/<id>', airlineFacade.update_flight),
    path('update-flight/', airlineFacade.update_flight_),
    path('flight-detail/<id>/', airlineFacade.flight_detail),

    path('remove/flight/<id>/', airlineFacade.remove_flight),


    path('my-flights/', airlineFacade.get_my_flights),

    # customerFacade URLS
    path('updatecustomer/<id>', customerFacade.update_customer),

    path('addticket', customerFacade.add_ticket),


    path('remove/tickets/<id>', customerFacade.remove_ticket),
    path('mytickets', customerFacade.get_my_tickets),

    # administratorFacade URLS
    path('customers', administratorFacade.get_all_customers),
    path('addairline', administratorFacade.add_airline),

    path('addcustomerr',administratorFacade.add_customer),
    path('addadmin',administratorFacade.add_administrator),
    path('removeairline/<id>',administratorFacade.remove_airline),
    path('removecustomer/<id>',administratorFacade.remove_customer),
    path('removeadmin/<id>',administratorFacade.remove_administrator),


    # path('users', customersView.myUsers),
    path('get-customer-profile', customersView.customer_profile),



    path('place-customer', customersView.place_customer),

    # path('users/<id>', customersView.myUsers),
    path('token/', anonymousFacade.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('login',TokenObtainPairView.as_view() ),
]
    

