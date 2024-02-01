from django.urls import path
from . import views

urlpatterns = [
    path('dz2/', views.index, name='main_2'),
    path('users2/', views.all_Users2_view, name='all_Users2'),
    path('products2/', views.all_Products2_view, name='all_products2'),
    ]
