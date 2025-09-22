from django.db import models
import os

class UserModel(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'UserModel'



class Company(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    profile = models.FileField(upload_to=os.path.join('static', 'Company_Profiles'), null=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'Company'


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    quantity = models.IntegerField()
    total_qty = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Products'


class Orders(models.Model):
    customer = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default='pending')
    ord_qty = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.customer.full_name
    
    class Meta:
        db_table = 'Orders'




