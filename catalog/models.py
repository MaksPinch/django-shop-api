from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL-адрес')
    image = models.ImageField(upload_to='categories/', verbose_name='Изображение')

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL-адрес')
    image = models.ImageField(upload_to='subcategories/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', verbose_name='Категория')

    def __str__(self):
        return f'{self.category.name}: {self.name}'

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL-адрес')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products', verbose_name='Подкатегория')

    def __str__(self):
        return self.name
