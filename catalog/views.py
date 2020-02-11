from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)


def category(request, slug):
    categ = Category.objects.get(slug=slug)
    context = {
        'current_category': categ,
        'product_list': Product.objects.filter(category=categ),
    }
    return render(request,'catalog/category.html', context)


def product(request, slug):
    produc = Product.objects.get(slug=slug)
    context = {
        # 'current_category': produc.category,
        'product_list': produc,
    }
    return render(request, 'catalog/product.html',context)