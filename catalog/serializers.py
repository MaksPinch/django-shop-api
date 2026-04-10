from rest_framework import serializers
from .models import Category, Subcategory, Product

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'slug', 'image', 'category']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'subcategories']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='subcategory.category.name')
    image_large = serializers.ImageField(read_only=True)
    image_medium = serializers.ImageField(read_only=True)
    image_small = serializers.ImageField(read_only=True)

    class Meta:
        model = Product
        fields = ['id','name', 'slug', 'category', 'subcategory','price', 'image', 'image_large', 'image_medium', 'image_small']
