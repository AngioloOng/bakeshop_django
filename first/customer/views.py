from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Product

def customer_home(request):
    # Home page view, possibly a landing page or product listing
    return render(request, 'customer_home.html')

def customer_login(request):
    # View for the login page
    return render(request, 'customerLogin.html')

def customer_signup(request):
    # View for the signup page
    return render(request, 'customerSignUp.html')

def customer_dashboard(request):
    # Dashboard view where authenticated users can access their info
    return render(request, 'customerDashboard.html')

def customer_about(request):
    # Logic for the "About" page can be added here
    return render(request, 'customerAbout.html')  # Point to the correct template

def view_products(request):
    products = Product.objects.all()  # Fetches all products from the database
    return render(request, 'view-products.html', {'products': products})

def orders(request):
    # Logic for displaying user orders
    return render(request, 'customerOrderStatus.html')  # Ensure you have this template

def payment_options(request):
    # Logic for displaying payment options
    return render(request, 'customerPaymentOption.html')  # Ensure you have this template

def delivery_settings(request):
    # Logic for displaying and updating delivery settings
    return render(request, 'customerDeliverySettings.html')  # Ensure you have this template

def support_messages(request):
    # Logic for displaying support messages
    return render(request, 'customerMessages.html')  # Ensure you have this template





# Your other view functions...

@require_POST
def set_delivery_options(request):
    # Example implementation, adjust according to your models and needs
    if request.user.is_authenticated:
        # Logic to update the user's delivery options based on form data
        # You might access form data using request.POST.get('<field_name>')
        # e.g., address = request.POST.get('address')
        
        # After updating the options, redirect to a confirmation page or back to the form
        return redirect('delivery_settings')  # Redirect to the delivery settings page
    else:
        # Redirect to login page if the user is not authenticated
        return redirect('customer_login')




from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST

# Import any necessary models or utilities

# from django.shortcuts import render
# from .models import Message  # Adjust the import according to your app structure

# def support_messages(request):
#     # Ensure the user is authenticated
#     if not request.user.is_authenticated:
#         return redirect('customer_login')

#     # Fetch message history for the current user
#     # Adjust the query to match your data model and relationships
#     messages = Message.objects.filter(recipient=request.user).order_by('-date_sent')

#     context = {
#         'messages': messages,
#     }
#     return render(request, 'customerMessages.html', context)




@require_POST
def send_message(request):
    # Implement the logic to handle the message submission
    # This might involve saving the message to the database
    
    # Make sure to check if the user is authenticated (if necessary)
    if not request.user.is_authenticated:
        return redirect('customer_login')  # Or wherever you want unauthenticated users to go

    # Example logic (adapt based on your model and fields)
    message_content = request.POST.get('message')
    if message_content:
        # Assuming you have a Message model and a way to identify the sender
        # Message.objects.create(content=message_content, sender=request.user)

        return redirect('customer_messages')  # Redirect to the messages page or confirmation page
    else:
        # Handle the case where the message is empty or invalid
        return HttpResponse('Invalid message content', status=400)