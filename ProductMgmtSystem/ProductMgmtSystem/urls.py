"""ProductMgmtSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,re_path,include
from django.conf import settings
# from djoser.views import TokenCreateView

from .views import IndexView
from django.contrib.staticfiles import views

from users.views import TokenCreateView,TokenDestroyView


urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    # path('product/', include('Product.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('Product.urls')),
    path('api/v1/login/', TokenCreateView.as_view(), name='login'),
    path('api/v1/logout/',TokenDestroyView.as_view(),name='logout'),
    path('api/v1/', include('users.urls')),

]


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]