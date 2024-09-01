from django.http import HttpResponse
from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort_item = request.GET.get('sort', 'name')
    if sort_item == 'min_price':
        sort = 'price'
    elif sort_item == 'max_price':
        sort ='-price'
    else:
        sort = 'name'
    phone_object = Phone.objects.order_by(sort)
    
    context = {
            'phones': phone_object,
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.all()
    context = {
            'phone': phone_object.filter(slug=slug).first(),
    }
    return render(request, template, context)
 
