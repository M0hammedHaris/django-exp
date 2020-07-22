from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard),
    path('customer/', views.customer),
    path('about/', views.about),
    path('contact/', views.contact),
]
