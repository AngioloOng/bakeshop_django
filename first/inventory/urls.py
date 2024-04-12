from . import views
from django.urls import path
from django.contrib import admin
from django.urls import include, path



app_name = 'inventory'
urlpatterns = [
    
    
    # path('', views.home, name="dashboard"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),

    path('admin/', admin.site.urls),
    #  path('customer/', views.customer_dashboard, name='customer_dashboard'),
    path('customer/', include('customer.urls', namespace='customer')),
    
    path('create_item/', views.createItem, name='create_item'),
    path('update_item/<str:pk>/', views.updateItem, name='update_item'),
    path('delete_item/<str:pk>/', views.deleteItem, name='delete_item'),
    path('delivery/', views.delivery, name="delivery"),
    path('create_order/', views.createDeliveryOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateDeliveryOrder, name='update_order'),
    path('deleteDelivOrder/<str:pk>/', views.deleteDeliveryOrder, name='deleteDelivOrder'),
]
