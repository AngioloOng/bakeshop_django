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
