from .views import ProductView
from django.urls import path,include
from rest_framework import routers

route=routers.DefaultRouter()
route.register(r'products',ProductView)



urlpatterns = [
    path("",include(route.urls))
]
