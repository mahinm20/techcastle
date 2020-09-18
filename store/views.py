from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items=order.orderitem_set.all()
        cartitems = order.get_cart_item
        
    else:
        items = []                
        order = {'get_cart_total':0,'get_cart_item':0,'shipping':False} 
        cartitems = order['get_cart_item']
    
    
    mobile = Mobile.objects.all()
    # laptop = Laptop.objects.all()
    # acc = Accessories.objects.all()
    context = {'mobile':mobile,'cartitems':cartitems}
    return render(request,'store/store.html',context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items=order.orderitem_set.all()
        cartitems = order.get_cart_item
        
    else:
        items = []                        
        order = {'get_cart_total':0,'get_cart_item':0}
        cartitems = order['get_cart_item']    

    context = {'items':items, 'order':order,'cartitems':cartitems, 'shipping':False}
    return render(request,'store/cart.html',context)


def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items=order.orderitem_set.all()
        cartitems = order.get_cart_item
        
    else:
        items = []      
        order = {'get_cart_total':0,'get_cart_item':0}
        cartitems = order['get_cart_item']    

    context = {'items':items, 'order':order,'cartitems':cartitems, 'shipping':False}
    

    
    return render(request,'store/checkout.html',context)    




# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     print('productId' , productId)
#     print('action ', action)


#     customer = request.user.customer
#     product_m = Mobile.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(customer=customer,completed=False)
#     orderItem, created = OrderItem.objects.get_or_create(order=order, product_m=product_m)

#     if action == "add":
#         orderItem.quantity == (orderItem.quantity+1)
#     elif action == "remove":
#         orderItem.quantity == (orderItem.quantity -1)

#     orderItem.save()

#     if orderItem.quantity <=0:
#         orderItem.delete()        


#     return JsonResponse('item was added', safe=False)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product_m = Mobile.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, completed=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product_m=product_m)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)



def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)

    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,completed=False)
        total=float(data['form']['total'])
        order.transaction_id=transaction_id

        if total==order.get_cart_total:
            order.completed=True
        order.save()

        if order.shipping ==True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode'],
            )
    else:
        print('user not logged in')

    return JsonResponse('payemnt submitted...',safe=False)            