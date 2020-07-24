from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .filters import *
from .forms import OrderForm
# Create your views here.


def home(request):
    return render(request, 'logestics/index.html')


def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count
    total_orders = orders.count
    pending_orders = orders.filter(status='Pending').count()
    delivered_orders = orders.filter(status='Delivered').count()

    context = {
        'customers': customers,
        'orders': orders,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
    }
    return render(request, 'logestics/dashboard.html', context=context)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count
    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs
    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_orders,
        'order_filter': order_filter,
    }
    return render(request, 'logestics/customer.html', context=context)


def createOrder(request):
    action = 'create'
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/dashboard')
    context = {'action': action, 'form': form}
    return render(request, 'logestics/order_form.html', context)


def updateOrder(request, pk):
    action = 'update'
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/customer/' + str(order.customer.id))

    context = {'action': action, 'form': form}
    return render(request, 'logestics/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        customer_id = order.customer.id
        customer_url = '/customer/' + str(customer_id)
        order.delete()
        return redirect(customer_url)
    return render(request, 'logestics/delete.html', {'item': order})
