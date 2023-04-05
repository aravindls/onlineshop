from django.urls import path
from .views import ProductList, FilterProductVIew

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('filter/', FilterProductVIew.as_view(), name='product-filter'),
]
