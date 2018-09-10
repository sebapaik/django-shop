from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Order
from django.views.generic import ListView, DetailView, CreateView

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'shop/index.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'
    ordering = ['id']

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product.html'
    context_object_name = 'products'
