from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard),
    path('customer/', views.customer),
    path('about/', views.about),
    path('contact/', views.contact),
]
