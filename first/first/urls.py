"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from inventory.views import home  # Adjust the import based on where your view is located


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('customer/', include('customer.urls')),
    path('', home, name='home'),  # Direct the root path to the home view

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)