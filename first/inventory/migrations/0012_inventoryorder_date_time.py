# Generated by Django 4.2.10 on 2024-04-16 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_inventoryitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryorder',
            name='date_time',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
