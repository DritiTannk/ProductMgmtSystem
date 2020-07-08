from rest_framework import viewsets  # To return API Data from views
from rest_framework.response import Response
from rest_framework import status  # It sends back the server status.
from .models import Product  # Our App Model
from .serializers import ProductSerializer  # Model Serializer.


# Create your views here.

class ProductDetailsViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer




