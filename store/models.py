from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name= models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name

class Mobile(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url                

class Laptop(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url      

class Accessories(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url      

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems  = self.orderitem_set.all()
        total = sum([item.get_laptop_total for item in orderitems])
        return total      
    
    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 
    
    

	 


class OrderItem(models.Model):
    product_m = models.ForeignKey(Mobile,on_delete=models.SET_NULL,null=True,blank=True)
    product_l = models.ForeignKey(Laptop,on_delete=models.SET_NULL,null=True,blank=True)
    product_a = models.ForeignKey(Accessories,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if (self.product_l is not None):
            return (self.product_l.name)
        elif (self.product_a is not None):
            return (self.product_a.name)
        elif (self.product_m is not None):
            return (self.product_m.name)    

    @property
    def get_mobile_total(self):
        total_m =  self.product_m.price * self.quantity
        return total_m    

    @property
    def get_acc_total(self):
        total_a =  self.product_a.price * self.quantity
        return total_a   
    
    @property
    def get_laptop_total(self):
        total_l =  self.product_l.price * self.quantity
        return total_l                      
    
   
    

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=200,null=False)
    city = models.CharField(max_length=200,null=False)
    zipcode = models.CharField(max_length=200,null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
