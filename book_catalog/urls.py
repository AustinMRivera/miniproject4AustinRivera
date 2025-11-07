# INF601 - Advanced Programming in Python
# Austin Rivera
# Mini Project 4

"""book_catalog URL Configuration
This sets up the main URLs for the project. I included the admin and auth URLs here.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('catalog_app.urls')),
]
