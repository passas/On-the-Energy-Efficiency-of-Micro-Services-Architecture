from django.urls import path
from . import views

urlpatterns = [
    path("invoice/order", views.order_invoice.as_view()),
]