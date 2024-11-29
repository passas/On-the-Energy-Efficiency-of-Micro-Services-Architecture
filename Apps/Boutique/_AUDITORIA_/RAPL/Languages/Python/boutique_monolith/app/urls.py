from django.urls import path
from . import views

urlpatterns = [
    path ("", view=views.index, name="index"),

    path ("login", view=views.login_view, name="login"),
    path ("logout", view=views.logout_view, name="logout"),
    path ("register", view=views.register, name="register"),

    path ("products/man", view=views.man, name="man"),
    path ("products/woman", view=views.woman, name="woman"),
    path ("products/man/<str:category>", view=views.man_category, name="man_category"),
    path ("products/woman/<str:category>", view=views.woman_category, name="woman_category"),
    path ("products/<int:id>", view=views.product_id, name="product_id"),
    
    path ("add-to-cart", view=views.add_to_cart, name="add-to-cart"),
    path ("cart", view=views.cart, name="cart"),

    path("cart/purchase", view=views.purchase, name="purchase"),

    path("orders", view=views.orders, name="orders"),
]