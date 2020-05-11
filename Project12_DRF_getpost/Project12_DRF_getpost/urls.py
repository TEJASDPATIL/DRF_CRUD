"""Project12_DRF_getpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt

from app12 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('product/',csrf_exempt(views.ProductOperations.as_view()),name="product"),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('list/',views.ProductListView.as_view(),name="list_products"),
    path('create/',views.ProductCreateApiView.as_view(),name="create"),
    path('detail/<int:pk>/',views.ProductDetailApiView.as_view(),name="detail"),
    path('delete/<int:pk>/',views.ProductDeleteApiView.as_view(),name="delete"),

]
