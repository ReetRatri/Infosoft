from django.urls import path
from . import views
from .views import *


urlpatterns = [
    # path('', views.item_list, name='item_list'),
    # path('index/', views.index),
    path('books/', views.book_list, name='book_list'),
    path('author/', views.author_list, name='author_list'),
    path('get_Employee_Project/', views.get_Employee_Project, name='get_Employee_Project'),
    
    ]