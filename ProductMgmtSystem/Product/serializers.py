from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        """
        This method will Validate the user data and serialize it.
        """
        if attrs['product_mrp'] <= 0:
            raise serializers.ValidationError("Price Cannot Be Zero or Negative.")
        return attrs

    class Meta:
        model = Product
        fields = ['product_name', 'manufacture_date',
                  'expiry_date', 'product_mrp',
                  'manufacture_name'
                  ]

    def update(self, instance, validated_data):
        """
        This method will update the record.
        """
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.product_mrp = validated_data.get('product_mrp', instance.product_mrp)
        instance.save()
        return instance
