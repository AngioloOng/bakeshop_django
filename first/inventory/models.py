from django.db import models

# Create your models here.

# class inventoryItem(models.Model):
# 	name = models.CharField(max_length = 100, null=True)
# 	description = models.CharField(max_length = 200, null=True)
# 	quantity = models.FloatField(null=True)
# 	unit = models.CharField(max_length = 5, null=True)
# 	item_pic = models.ImageField(null=True, blank=True)

# 	def __str__(self):
# 		return self.name

from django.db import models

# class Vendor(models.Model):
#     name = models.CharField(max_length=100)
#     # Add other vendor fields as needed

#     def __str__(self):
#         return self.name

class inventoryItem(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)
    quantity = models.FloatField(null=True)
    unit = models.CharField(max_length=5, null=True)
    price = models.FloatField(null=True)
    item_pic = models.ImageField(null=True, blank=True)
    # price = models.DecimalField(max_digits=8, decimal_places=2, null=True)  # Adding a price field
    # vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
class inventoryOrder(models.Model):
	PAID = "Paid"
	NOT_PAID = "Not Paid"
	PAYMENT_STATUS_CHOICES = [
		(PAID, 'Paid'), (NOT_PAID, 'Not Paid')
	]
	name = models.CharField(max_length = 100, null=True)
	address = models.CharField(max_length = 200, null=True)
	paid_Status = models.CharField(
		max_length=8,
        choices=PAYMENT_STATUS_CHOICES,
        default=NOT_PAID,
		)
	order = models.CharField(max_length = 60, null=True)

	def __str__(self):
		return self.name