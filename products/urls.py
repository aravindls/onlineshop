from django.urls import path
from .views import ProductList, FilterProductVIew

urlpatterns = [
    path('', ProductList.as_view(), name='productlist'),
    path('filter/', FilterProductVIew.as_view(), name='product-filter'),
]
