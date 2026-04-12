from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import CartSerializer, CartItemSerializer
from catalog.models import Product
from .models import CartItem

# Create your views here.
class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CartSerializer(user)
        return Response(serializer.data)

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity= request.data.get('quantity', 1)

        if not product_id:
            return Response(
                'Не указан ID товара'
            )

        try:
            product_id = int(product_id)
            quantity = int(quantity)
        except (ValueError, TypeError):
            return Response(
                'ID товара и количество должны быть числами'
            )

        desired_product = Product.objects.filter(id=product_id).first()

        if desired_product is None:
            return Response('Товар не найден', status=404)

        item = CartItem.objects.filter(user=request.user, product=desired_product).first()

        if item is not None:
            item.quantity += quantity
            item.save()
        else:
            CartItem.objects.create(
                user=request.user,
                product=desired_product,
                quantity=quantity
            )

        return Response('Успешно добавлено')

    def delete(self, request):
        product_id = request.data.get('product_id')

        if product_id:
            CartItem.objects.filter(user=request.user, product_id=product_id).delete()
            return Response('Товар удален из корзины')
        else:
            CartItem.objects.filter(user=request.user).delete()
            return Response('Корзина полностью очищена')

