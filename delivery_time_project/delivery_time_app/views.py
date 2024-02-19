from rest_framework import viewsets
from .models import Customer, FoodMenu, Restaurant, Order
from .serializers import CustomerSerializer, FoodMenuSerializer, RestaurantSerializer, OrderSerializer
from django.shortcuts import render
import io
from django.utils import timezone
from datetime import timedelta
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
import requests
from openrouteservice import client

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class FoodMenuViewSet(viewsets.ModelViewSet):
    queryset = FoodMenu.objects.all()
    serializer_class = FoodMenuSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
 
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        # Retrieve customer and restaurant coordinates
        customer_id = request.data.get('customer')
        restaurant_id = request.data.get('restaurant')

        try:
            customer = Customer.objects.get(pk=customer_id)
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Customer.DoesNotExist:
            return Response({'error': 'Customer not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Restaurant.DoesNotExist:
            return Response({'error': 'Restaurant not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Ensure that both customer and restaurant coordinates are available
        if customer.latitude is not None and customer.longitude is not None \
                and restaurant.latitude is not None and restaurant.longitude is not None:
            # Calculate estimated time based on distance between customer and restaurant
            ORS_API_KEY = '5b3ce3597851110001cf6248792eb2af457e45ceb3587b806a1b376e'
            url = 'https://api.openrouteservice.org/v2/directions/driving-car'
            params = {
                'coordinates': [[customer.longitude, customer.latitude], [restaurant.longitude, restaurant.latitude]],
                'profile': 'driving-car',
                'format': 'json',
                'optimize_waypoints': False
            }

            # Include headers with API key
            headers = {
                'Authorization': f'Bearer {ORS_API_KEY}',
                'Content-Type': 'application/json; charset=utf-8'
            }

            # Make request to OpenRouteService API with headers
            response = requests.get(url, json=params, headers=headers)
            print(response)

            if response.status_code == 200:
                try:
                    data = response.json()
                    print (data)
                    # Extract duration from response and calculate estimated arrival time
                    duration_traffic = data['routes'][0]['summary']['duration']
                    estimated_duration_hours = duration_traffic / 3600
                    estimated_arrival = timezone.now() + timedelta(hours=estimated_duration_hours)
                    print(estimated_arrival)
                    # Update request data with estimated arrival time
                    request.data['estimated_time'] = estimated_arrival
                except Exception as e:
                    return Response({'error': 'Error processing response from OpenRouteService API'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'error': 'Failed to fetch data from OpenRouteService API'}, status=response.status_code)
        else:
            return Response({'error': 'Customer or restaurant coordinates are missing'}, status=status.HTTP_400_BAD_REQUEST)

        # Proceed with creating the order
        return super().create(request, *args, **kwargs)
