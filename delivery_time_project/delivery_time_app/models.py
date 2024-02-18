from django.db import models
from django.utils import timezone
from datetime import timedelta
import osmnx as ox
from openrouteservice import client
from geopy.geocoders import Photon

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            geolocator = Photon(user_agent="measurements")
            location = geolocator.geocode(self.address)
            self.latitude = location.latitude
            self.longitude = location.longitude
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username


class FoodMenu(models.Model):
    food_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    food_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.food_name


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            geolocator = Photon(user_agent="measurements")
            location = geolocator.geocode(self.address)
            self.latitude = location.latitude
            self.longitude = location.longitude
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    food = models.ForeignKey(FoodMenu, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    estimated_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.order_id} for {self.customer.username}"
