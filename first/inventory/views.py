from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
	return render(request, 'inventory/dashboard.html')

def inventory(request):
	item = inventoryItem.objects.all()
	return render(request, 'inventory/inventory.html', {'item': item})

def customer(request):
	return render(request, 'inventory/customer.html')

