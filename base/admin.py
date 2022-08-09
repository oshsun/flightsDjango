from django.contrib import admin
from .models import AirlineCompany, Country, Customer, Flight, Ticket, UserRole ,Adminstrator,MyUserProfile

 
admin.site.register(AirlineCompany)
admin.site.register(MyUserProfile)
admin.site.register(Country)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Customer)
admin.site.register(UserRole)
admin.site.register(Adminstrator)