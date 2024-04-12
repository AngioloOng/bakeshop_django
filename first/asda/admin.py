from django.contrib import admin
from .models import Product, Message, User

# Register your models here.
admin.site.register(Product)
admin.site.register(Message)

# Customize the User model admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  # Fields to display in the list view
    search_fields = ['name', 'email']  # Fields to search in the admin interface
    # Add more customization as needed

admin.site.register(User, UserAdmin)
