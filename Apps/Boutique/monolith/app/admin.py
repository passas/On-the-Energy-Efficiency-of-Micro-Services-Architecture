from django.contrib import admin
from .models import Product, Sex, Category, Material, Color, Stock, Price
from .models import Cart, CartProduct
from .models import Payment, PaymentMethod
from .models import Order, OrderProduct
from .models import Shipping, ShippingMethod

class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ("materials",)

class CartAdmin(admin.ModelAdmin):
    filter_horizontal = ("products",)

class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ("products",)

admin.site.register (Product, ProductAdmin)
admin.site.register (Sex)
admin.site.register (Material)
admin.site.register (Color)
admin.site.register (Stock)
admin.site.register (Price)
admin.site.register (Category)

admin.site.register (Cart, CartAdmin)
admin.site.register (CartProduct)

admin.site.register (Payment)
admin.site.register (PaymentMethod)

admin.site.register (Order, OrderAdmin)
admin.site.register (OrderProduct)

admin.site.register (Shipping)
admin.site.register (ShippingMethod)