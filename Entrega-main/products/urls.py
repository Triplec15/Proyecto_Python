from django.urls import path
from django.contrib import admin
from products.views import products, contacto, categoria, create_product_view, search_product_view

urlpatterns =[
    path('', products, name = 'products'),
    path('contacto/', contacto, name = 'contacto'),
    path('categoria/', categoria, name = 'categoria'),
    path('create-product/', create_product_view, name = 'create-product'),
    path('search-product/', search_product_view, name = 'search_product_view')
]





