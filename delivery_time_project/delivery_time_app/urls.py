from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'foodmenus', views.FoodMenuViewSet)
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('customer/',views.customer_api)
]
