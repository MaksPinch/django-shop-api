from rest_framework import serializers
from .models import CartItem
from catalog.serializers import ProductSerializer
from django.contrib.auth.models import User
from django.db.models import Sum, F

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'total_price']


    def get_total_price(self, obj):
        return obj.quantity * obj.product.price


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(read_only=True, many=True)
    cart_sum = serializers.SerializerMethodField()
    cart_items_quantity = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['cart_items', 'cart_sum', 'cart_items_quantity']

    def get_cart_items_quantity(self, obj):
        quantity_data = obj.cart_items.aggregate(
            total_quantity=Sum('quantity')
        )

        result = quantity_data.get('total_quantity')

        if result is not None:
            return result
        else:
            return 0

    def get_cart_sum(self, obj):
        total_sum_data = obj.cart_items.aggregate(
            total_sum=Sum(F('quantity') * F('product__price'))
        )

        result = total_sum_data.get('total_sum')

        if result is not None:
            return result
        else:
            return 0

