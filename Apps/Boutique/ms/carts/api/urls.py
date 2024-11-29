from django.urls import path
from . import views

urlpatterns = [
    path("cart", views.cart.as_view()),
    path("cart/purchase", views.purchase.as_view()),
]