from django.urls import path
from . import views

urlpatterns = [
    path ("", view=views.index, name="index"),

    path ("login", view=views.login, name="login"),
    path ("logout", view=views.logout, name="logout"),
    path ("register", view=views.register, name="register"),

    path ("man", view=views.man, name="man"),
    path ("woman", view=views.woman, name="woman"),
    path ("man/<str:category>", view=views.man_category, name="man_category"),
    path ("woman/<str:category>", view=views.woman_category, name="woman_category"),
    path ("<int:id>", view=views.product, name="product"),

    path ("cart", view=views.cart, name="cart"),
    path ("cart/purchase", view=views.cart_purchase, name="cart_purchase"),
]