from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    http_method_names = ['get']
    template_name = 'product.html'