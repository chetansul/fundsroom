from django.contrib import admin
from django.urls import path, include
#from delivery_time_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('delivery_time_app.urls')),
]
