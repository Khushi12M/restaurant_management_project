from django.contrib import admin
from .models import MenuItem, order

class MenuItemAdmin(admin.ModelAdmin):
    list_dispaly=("id", "name", "price", "is_available", "restaurant", "created_at")
    list_filter =("is_available", "restaurant")
    search_fields =("name", "description")

    class OrderAdmin(admin.ModelAdmin):
        list_dispaly =("id", "restaurant", "customer_name", "status", "created_at")
        list_filter =("status", "restaurant")
        search_fields =("customer_name", "restaurant_name")