from django.forms import ModelForm
from .models import inventoryItem, inventoryOrder

class itemForm(ModelForm):
    class Meta:
        model = inventoryItem
        fields = '__all__'

class orderForm(ModelForm):
    class Meta:
        model = inventoryOrder
        fields = '__all__'

# PRODUCTS FORMS
from django import forms
from .models import ProductItem

class ProductItemForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        fields = ['name', 'description', 'price', 'quantity', 'image']
