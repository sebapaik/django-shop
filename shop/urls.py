from django.urls import path
from .views import ProductListView, ProductDetailView
from . import views

urlpatterns = [
    #path('', views.index, name = 'shop-index'),
    path('', ProductListView.as_view(), name = 'shop-index'),
    path('<int:pk>/', ProductDetailView.as_view(), name = 'shop-product'),
]
