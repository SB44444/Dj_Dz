from django.urls import path
from . import views


urlpatterns = [
    path('3/', views.index, name='main_3'),
    path('3/all_users/', views.all_Users3_view, name='all_Users3'),
    path('3/all_prducts/', views.all_Products3_view, name='all_products3'),
    path('3/get_order_by_id/<int:user_id>/', views.user_Order, name='user_order_by_id'),
    path('3/week_user_order/<int:user_id>/', views.week_order, name='week_user_orders'),
    path('3/monht_user_order/<int:user_id>/', views.month_order, name='month_user_orders'),
    path('3/year_user_order/<int:user_id>/', views.year_order, name='year_user_orders'),
    ]
