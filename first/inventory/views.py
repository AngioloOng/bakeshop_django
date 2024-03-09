from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'inventory/dashboard.html')

def inventory(request):
	return render(request, 'inventory/inventory.html')

def customer(request):
	return render(request, 'inventory/customer.html')

