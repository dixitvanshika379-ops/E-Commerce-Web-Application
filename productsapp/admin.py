from django.contrib import admin
from .models import Product, Order


admin.site.register(Product)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'status', 'total_amount', 'created_at')