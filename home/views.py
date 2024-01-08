from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
# Create your views here.  
def home(request):
    return render(request, 'index.html')

def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request, 'cart.html',{'cart':cart})
    else:
        return redirect('/')
def add_to_cart(request):
    if request.headers.get('X-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=(data['product_qty'])
            product_id=(data['pid'])
            # print(request.user.id)
            product_status=pro.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id, product_id=product_id):
                    return JsonResponse({'status':'Product already added'},status=200)
                else:
                    if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
                        return JsonResponse({'status':'product added to cart'},status=200)
                    else:
                        return JsonResponse({'status':'No stock'},status=200)
            return JsonResponse({'status':'Product added to cart successfully'},status=200)
        else:
            return JsonResponse({'status':'Login to Add cart'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)

def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect('/cart')

def collections(request):
    category=cat.objects.filter(status=0)
    return render(request,'collections.html', {'category':category})
def products(request):
    return render(request, 'products.html')
def collectionsView(request, name):
    if (cat.objects.filter(name=name, status=0)):
        products=pro.objects.filter(category__name=name)
        return render(request,'products.html', {'products':products, 'category_name':name})
    else:
        messages.warning(request, 'no such category found')
        return redirect('collections')

def product_info(request,cname, pname):
    if(cat.objects.filter(name=cname, status=0)):
        if(pro.objects.filter(name=pname, status=0)):
            products=pro.objects.filter(name=pname,status=0).first()
            return render(request,'pro_details.html',{'products':products})
        else:
            messages.error(request, 'no such product found')
            return redirect('collections')
    else:
        messages.error(request, 'no such category found')
        return redirect('collections')
