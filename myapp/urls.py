from django.urls import path
from . import views
from .views import *
# from .views import index
from .models import Item

urlpatterns = [
    # path('', views.item_list, name='item_list'),
    path('index/', views.index),
    path('create/', views.create_item, name='create_item'),
    path('update/<int:pk>/', views.update_item, name='update_item'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),

    path('form/', views.form, name='form'),
    path('success/', views.success_view, name='success'),
    path('search/', views.searchbox, name='searchbox'),
    path('login/', views.login_portal, name='login_portal'),
    path('', views.registration_portal, name='registration_portal'),
    path('logout/', logout_portal, name='logout'),


]
