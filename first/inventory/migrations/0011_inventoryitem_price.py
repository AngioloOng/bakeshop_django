# Generated by Django 5.0.3 on 2024-04-14 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_remove_inventoryitem_vendor_delete_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]