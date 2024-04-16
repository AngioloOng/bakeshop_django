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

def inventory_dashboard(request):
	return render(request, 'inventory/dashboard.html')



from customer.models import CartItem
def new_order(request):
    orders = CartItem.objects.all()
    return render(request, 'inventory/new_orders.html', {'orders': orders})
	




def customer(request):
	return render(request, 'inventory/customer.html')

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
			return redirect('/inventory/inventory')

	context = {'form': form}
	return render(request, 'inventory/item_form.html', context)

# def deleteItem(request, pk):
# 	item = inventoryItem.objects.get(id=pk)

# 	if request.method == "POST":
# 		item.delete()
# 		return redirect('inventory')
# 	context = {'item': item}
# 	return render(request, 'inventory/delete.html', context)

from django.shortcuts import render, redirect, get_object_or_404

def deleteItem(request, pk):
    # Use get_object_or_404 to safely get the item
    item = get_object_or_404(inventoryItem, id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('inventory:inventory')  # Ensure this redirect is correct
    context = {'item': item}
    return render(request, 'inventory/delete.html', context)


def delivery(request):
	order = inventoryOrder.objects.all()
	return render(request, 'inventory/delivery.html', {'order': order})

def createDeliveryOrder(request):
	form = orderForm()
	if request.method == 'POST':
		form = orderForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/inventory/delivery')

	context = {'form': form}
	return render(request, 'inventory/order_form.html', context)

def updateDeliveryOrder(request, pk):
	order = inventoryOrder.objects.get(id=pk)
	form = orderForm(instance=order)

	if request.method == 'POST':
		form = orderForm(request.POST, request.FILES, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/inventory/delivery')

	context = {'form': form}
	return render(request, 'inventory/order_form.html', context)

def deleteDeliveryOrder(request,pk):
	order = inventoryOrder.objects.get(id=pk)

	if request.method == "POST":
		order.delete()
		return redirect('/inventory/delivery')

	context = {'order': order}
	return render(request, 'inventory/delete_order.html', context)

def all_orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'inventory/all_orders.html', context)