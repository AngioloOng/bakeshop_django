# Generated by Django 5.0.3 on 2024-04-12 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_vendor_inventoryitem_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryitem',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]
