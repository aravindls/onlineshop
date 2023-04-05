from django.http import Http404

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
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    
class FilterProductVIew(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_ids = self.request.query_params.getlist('category')
        queryset = Product.objects.all()

        if category_ids:
            queryset = queryset.filter(category__id__in=category_ids)

        return queryset