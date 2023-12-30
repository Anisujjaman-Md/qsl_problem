from django.urls import path
from rest_framework import routers
from qsl_ecom.views import ProductListView
router = routers.DefaultRouter()

# router.register()

urlpatterns = [path('products/', ProductListView.as_view(), name='product-list'), ] + router.urls
