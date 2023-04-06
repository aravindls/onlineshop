from django.shortcuts import render

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

class ProductList(APIView):
    def get(self, request,format=None):
        product_id = request.GET.get('product_id',None)
        if product_id:
            products = Product.objects.get(id = product_id)
            serializer = ProductSerializer(products) 
            return Response(serializer.data)   
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)

        categories = Category.objects.all()
        return render(request, 'product_list.html', {'products': serializer.data,'categories': categories})
    
    
class FilterProductVIew(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category_ids = self.request.GET.get('category')
        if category_ids:
            category_ids = list(map(int, category_ids.split(',')))
            queryset = queryset.filter(category__id__in=category_ids)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return render(request, 'product_list.html', {'products': serializer.data})