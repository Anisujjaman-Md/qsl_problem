from rest_framework import generics
from rest_framework import filters
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category__name', 'brand__name', 'seller__name']
    ordering_fields = ['price', 'created_at', 'updated_at']
