# Generated by Django 5.0.3 on 2024-04-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]