from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="dashboard"),
    path('dashboard/', views.home, name="dashboard"),
    path('inventory/', views.inventory, name='inventory'),
    path('customer/', views.customer, name='customer'),
    path('create_item/', views.createItem, name='create_item'),
    path('update_item/<str:pk>/', views.updateItem, name='update_item'),
    path('delete_item/<str:pk>/', views.deleteItem, name='delete_item'),
    path('delivery/', views.delivery, name="delivery"),
    path('create_order/', views.createDeliveryOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateDeliveryOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteDeliveryOrder, name='delete_order'),
]
