from django.urls import path
from . import views

urlpatterns = [
    path("pay", views.pay.as_view()),
]