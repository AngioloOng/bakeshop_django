from django.db import models

# Create your models here.

class inventoryItem(models.Model):
	name = models.CharField(max_length = 100, null=True)
	description = models.CharField(max_length = 200, null=True)
	quantity = models.FloatField(null=True)
	item_pic = models.ImageField(null=True, blank=True)

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