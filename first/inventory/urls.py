from . import views
from django.urls import path
from django.contrib import admin
from django.urls import include, path



app_name = 'inventory'

urlpatterns = [
    
    
    path('dashboard/', views.inventory_dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
    path('new_order/', views.new_order, name='new_order'),
    path('admin/', admin.site.urls),
    path('customer/', include('customer.urls', namespace='customer')),
    path('create_item/', views.createItem, name='create_item'),
    path('update_item/<str:pk>/', views.updateItem, name='update_item'),
    path('delete_item/<str:pk>/', views.deleteItem, name='delete_item'),    
    path('delivery/', views.delivery, name="delivery"),
    path('create_order/', views.createDeliveryOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateDeliveryOrder, name='update_order'),
    path('deleteDelivOrder/<str:pk>/', views.deleteDeliveryOrder, name='deleteDelivOrder'),
    path('all_orders/', views.all_orders, name='all_orders'),
    
    path('delete-order/<int:pk>/', views.deleteOrder, name='delete-order'),
    
    path('products/', views.products, name='products'),
    
    
    path('products/delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('products/', views.products, name='products'),  # Ensure this is intended for listing products
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/<str:pk>/', views.updateProduct, name='update_product'),

]
