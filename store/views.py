from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    mobile = Mobile.objects.all()
    laptop = Laptop.objects.all()
    acc = Accessories.objects.all()
    context = {'mobile':mobile,'laptop':laptop,'acc':acc}
    return render(request,'store/store.html',context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items=order.orderitem_set.all()
    else:
        items = []
                        
        order = {'get_cart_total':0}    

    context = {'items':items, 'order':order }
    return render(request,'store/cart.html',context)

def checkout(request):

    context = {}
    return render(request,'store/checkout.html',context)    