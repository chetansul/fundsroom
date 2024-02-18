from rest_framework import serializers
from .models import Customer, FoodMenu, Restaurant, Order

'''class customer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email =serializers.EmailField()
    mobile_number = serializers.CharField(max_length=15)
    address = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return customer.objects.create(**validated_data)
'''
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class FoodMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodMenu
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # Remove 'estimated_time' from fields
        fields = ['order_id','customer', 'food', 'restaurant',]
    