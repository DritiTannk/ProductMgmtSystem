from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'manufacture_date',
                  'expiry_date', 'product_mrp',
                  'manufacture_name'
                  ]
