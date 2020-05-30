from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, get_object_or_404  # When Object doest not exists it shows 404 error
from django.http import HttpResponse
from rest_framework.views import APIView  # To return API Data from views
from rest_framework.response import Response
from rest_framework import status  # It sends back the server status.
from .models import Product  # Our App Model
from .serializers import ProductSerializer  # Model Serializer.


# Create your views here.

class ProductList(APIView):

    def get(self,request):
        product_objects = Product.objects.all()
        serializer = ProductSerializer(product_objects,many=True)  # It states that there are mopre than 1 product object.
        return Response(serializer.data)

    def post():
        pass