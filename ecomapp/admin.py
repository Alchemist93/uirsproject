from django.contrib import admin
from ecomapp.models import Category, Brand, Product, CartItem, Cart

# Register your models here.
admin.register(Category)(admin.ModelAdmin)
admin.register(Brand)(admin.ModelAdmin)
admin.register(Product)(admin.ModelAdmin)
admin.register(Cart)(admin.ModelAdmin)
admin.register(CartItem)(admin.ModelAdmin)

