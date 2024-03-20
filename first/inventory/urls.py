from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="dashboard"),
    path('dashboard/', views.home, name="dashboard"),
    path('inventory/', views.inventory, name='inventory'),
    path('customer/', views.customer, name='customer'),
]
