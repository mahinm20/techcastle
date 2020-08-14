from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Mobile)
admin.site.register(Laptop)
admin.site.register(Accessories)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
