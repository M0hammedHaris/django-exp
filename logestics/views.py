from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'logestics/index.html')


def dashboard(request):
    return render(request, 'logestics/dashboard.html')


def customer(request):
    return render(request, 'logestics/customer.html')


def about(request):
    return render(request, 'logestics/about.html')


def contact(request):
    return render(request, 'logestics/contact.html')
