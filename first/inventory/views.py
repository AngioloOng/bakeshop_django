from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import itemForm
from .forms import orderForm

# Create your views here.

def home(request):
	return render(request, 'inventory/dashboard.html')

def inventory(request):
	item = inventoryItem.objects.all()
	return render(request, 'inventory/inventory.html', {'item': item})

def customer(request):
	return render(request, 'inventory/customer.html')

def delivery(request):
	order = inventoryOrder.objects.all()
	return render(request, 'inventory/delivery.html', {'order': order})

def createItem(request):
	form = itemForm()
	if request.method == 'POST':
		form = itemForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/inventory/inventory')

	context = {'form': form}
	return render(request, 'inventory/item_form.html', context)

def updateItem(request, pk):
	item = inventoryItem.objects.get(id=pk)
	form = itemForm(instance=item)

	if request.method == 'POST':
		form = itemForm(request.POST, request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return redirect('/inventory')

	context = {'form': form}
	return render(request, 'inventory/item_form.html', context)

def deleteItem(request, pk):
	item = inventoryItem.objects.get(id=pk)

	if request.method == "POST":
		item.delete()
		return redirect('inventory')
	context = {'item': item}
	return render(request, 'inventory/delete.html', context)

def createDeliveryOrder(request):
	form = orderForm()
	if request.method == 'POST':
		form = orderForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/inventory/inventory/delivery')

	context = {'form': form}
	return render(request, 'inventory/order_form.html', context)

def updateDeliveryOrder(request, pk):
	order = inventoryOrder.objects.get(id=pk)
	form = orderForm(instance=order)

	if request.method == 'POST':
		form = orderForm(request.POST, request.FILES, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/inventory/inventory/delivery')

	context = {'form': form}
	return render(request, 'inventory/order_form.html', context)

def deleteDeliveryOrder(request,pk):
	order = inventoryOrder.objects.get(id=pk)

	if request.method == "POST":
		order.delete()
		return redirect('/inventory/inventory/delivery')

	context = {'order': order}
	return render(request, 'inventory/order_form.html', context)

