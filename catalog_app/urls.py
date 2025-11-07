# INF601 - Advanced Programming in Python
# Austin Rivera
# Mini Project 4

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('about/', views.about, name='about'),
    path('login/', LoginView.as_view(template_name='catalog_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
