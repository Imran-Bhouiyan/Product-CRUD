from django.shortcuts import render,redirect, HttpResponse
from .models import Product ,SubCategory, Category

def index(request):
    context={
        'products' : Product.objects.all()
    }
    return render(request ,'index.html' , context)

def create(request):
    print(request.POST)
    product_code=request.GET['product_code']
    product_name=request.GET['product_name']
    description=request.GET['description']
    date=request.GET['date']
    price=request.GET['price']
    product_detail=Product(product_code=product_code, product_name=product_name,description=description,date=date,price=price)
    product_detail.save()
    return redirect('/')


def add_product(request):
    return render(request,'add_product.html')

def delete(request,id):
    products =Product.objects.get(pk=id)
    products.delete()
    return redirect('/')


def edit(request,id):
    products=Product.objects.get(pk=id)
    context={
        'products':products
    }
    return render(request,'edit.html',context)


def update(request,id):
    products=Product.objects.get(pk=id)
    product_code=request.GET['product_code']
    product_name=request.GET['product_name']
    description=request.GET['description']
    date=request.GET['date']
    price=request.GET['price']
    products.save()
    return redirect('/')






