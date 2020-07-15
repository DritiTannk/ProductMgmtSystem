from django.urls import path,include
from rest_framework import routers
from .views import ProductDetailsViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductDetailsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
