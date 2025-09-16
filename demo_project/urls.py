from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.views import ProductViewSet, weather, product_report, dashboard

# DRF router for CRUD endpoints
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),           # CRUD endpoints
    path('api/weather/', weather),               # Weather endpoint
    path('api/product_report/', product_report), # Product summary report
    path('dashboard/', dashboard)                # Dashboard page
]
