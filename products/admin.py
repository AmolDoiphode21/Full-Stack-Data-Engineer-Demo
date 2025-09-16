from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description')  # shown in table
    search_fields = ('name', 'description')  # search bar in admin
    list_filter = ('price',)  # add filters
