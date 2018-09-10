from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='cart-add'),
    path('', views.cart_detail, name='cart-detail'),
]
