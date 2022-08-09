from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError(
            (f"{value} is taken."),
            params = {'value':value}
        )

def validate_phone_num(phone_num: str):
    if len(phone_num) != 10:
        raise ValidationError(
           _('the phone number: %(phone_num)s is less then 10 digits'),
           params={'phone_num': phone_num},
        )
    for digit in phone_num:
        if  not digit.isdigit:
            raise ValidationError(
           _('The phone number should contain only numbers, you entered: %(phone_num)s '),
           params={'phone_num': phone_num},
        )

def validat_ecredit_card(credit_card: str):
    for digit in credit_card:
        if  not digit.isdigit:
            raise ValidationError(
            _('The credit card number should contain only numbers, you entered: %(credit_card)s '),
            params={'credit_card': credit_card},
            )

def validate_pwd(pwd:str):
    if len(pwd) < 6:
        raise ValidationError(
           _('the password must contain at least 6 characters'),
           params={'pwd': pwd},
        )

def validate_flight_tickets(flight_tickets:int):
    if flight_tickets < 0:
        raise ValidationError(
           _('flight remaining tickets can not be less than 0 '),
           params={'flight_tickets': flight_tickets},
        )

def validate_flight_time(departure_time:datetime,landing_time:datetime):
    if landing_time < departure_time:
        raise ValidationError(
           _('landing time can not be before departure time'),
           params={'departure_time': departure_time, 'landing_time': landing_time},
        )

def validate_destinaton(origin_country_id:int,destination_country_id:int):
    if origin_country_id == destination_country_id:
        raise ValidationError(
           _('flight destination must be different from the origin country'),
           params={'origin_country_id': origin_country_id, 'destination_country_id': destination_country_id},
        )


    # if value % 2 != 0:
    #     raise ValidationError(
    #         _('%(value)s is not an even number'),
    #         params={'value': value},
    #     )