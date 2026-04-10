from django.urls import path
from .views import CategoryListView, ProductListView
urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('categories/', CategoryListView.as_view())
]
