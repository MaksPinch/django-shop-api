from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User
# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items', verbose_name='Покупатель')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items', verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

def __str__(self):
    return f'{self.user.username}: {self.product.name} = {self.quantity}'


