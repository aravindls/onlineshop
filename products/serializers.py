from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    sub_category = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('name', 'description','price','category','sub_category')
        
    def get_category(self, obj):
        print(obj.category.values_list())
        category =dict(obj.category.values_list())
        return category
    
    def get_sub_category(self, obj):
        sub_category =dict(obj.subcategory.values_list('id','name'))
        return sub_category
