from django.urls import path
from .views import ProductList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/', ProductList.as_view(), name='product_api_view'),
]
