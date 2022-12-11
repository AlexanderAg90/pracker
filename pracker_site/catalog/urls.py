from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>/', views.show_category, name='category'),
    path('product/<slug:product_slug>/', views.show_product, name='pruduct'),
]