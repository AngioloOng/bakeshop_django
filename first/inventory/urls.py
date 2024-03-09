from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('inventory/', views.inventory),
    path('customer/', views.customer),
]