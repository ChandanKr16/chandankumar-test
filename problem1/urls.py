from django.urls import path, include
from . import views

urlpatterns = [
    path('numbers/', views.numbers),
    path('prefixes/', views.prefixes),
]

