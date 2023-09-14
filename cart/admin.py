from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('cart_id','created_at')

@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display=('product','user','quantity','is_active','id')