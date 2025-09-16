from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg, Max, Min, Count

from .models import Product
from .serializers import ProductSerializer
from .external_api import fetch_weather

# ----------------------------
# CRUD API for Product
# ----------------------------
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ----------------------------
# Weather API
# ----------------------------
@api_view(['GET'])
def weather(request):
    city = request.GET.get("city", "London")
    data = fetch_weather(city)
    return Response(data)

# ----------------------------
# Product Report API
# ----------------------------
@api_view(['GET'])
def product_report(request):
    report = Product.objects.aggregate(
        total_products=Count('id'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return Response(report)

# ----------------------------
# Dashboard View
# ----------------------------
def dashboard(request):
    return render(request, 'products/dashboard.html')
