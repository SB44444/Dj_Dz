from django.urls import path
from . import views

urlpatterns = [
    path('2', views.index, name='main_2'),
    path('users/', views.all_Users_view, name='all_Users'),
    path('products/', views.all_Products_view, name='all_products'),
    ]
