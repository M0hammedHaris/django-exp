from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    return render(request, 'logestics/index.html')


def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count
    total_orders = orders.count
    pending_orders = orders.filter(status = 'Pending').count()
    delivered_orders = orders.filter(status = 'Delivered').count()

    context = {
        'customers': customers,
        'orders': orders,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
    }
    return render(request, 'logestics/dashboard.html', context=context)


def customer(request):
    return render(request, 'logestics/customer.html')


def about(request):
    return render(request, 'logestics/about.html')


def contact(request):
    return render(request, 'logestics/contact.html')
