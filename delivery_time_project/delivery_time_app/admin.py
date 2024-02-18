from django.contrib import admin

from .models import Restaurant,FoodMenu,Customer,Order

# Register the Product model with the admin site
admin.site.register(Restaurant)
admin.site.register(FoodMenu)
admin.site.register(Customer)
admin.site.register(Order)