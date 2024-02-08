from django.urls import path
from . import views
from . views import update_product, update_client, upload_image


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user/add/', update_client, name='update_client'),
    path('product/add/', update_product, name='update_product'),
    path('upload_image/<int:product_id>', upload_image, name='upload_image')
    ]
