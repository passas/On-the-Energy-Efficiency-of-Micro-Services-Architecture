from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    re_path('api/login', views.login),
    re_path('api/register', views.register),
    re_path('api/authenticate', views.authenticate),

    re_path('api/auditoria', views.auditoria),
]