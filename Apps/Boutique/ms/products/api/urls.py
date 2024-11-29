from django.urls import path
from . import views

urlpatterns = [
    
    path("man", views.man.as_view()),
    path("woman", views.woman.as_view()),

    path("man/categories", views.man_categories.as_view()),
    path("woman/categories", views.woman_categories.as_view()),
    
    path("man/<str:category>", views.man_category.as_view()),
    path("woman/<str:category>", views.woman_category.as_view()),
    
    path("<int:id>/<str:size>", views.get_product.as_view()),
    path("<int:id>", views.id.as_view()),
    path("bulk", views.bulk.as_view()),
]