from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
import random


main_links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'products:index', 'name': 'Продукты'},
        {'href': 'contact', 'name': 'Контакты'}
    ]


def get_hot_product():
    _products = get_products()
    return random.sample(list(_products), 1)[0]

    
def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products

def main(request):
    title = 'Главная'
    content = {
            'title': title,
            'links_menu': main_links_menu,          
        }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = 'Категории'
    categories = get_categories()
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    if pk is not None:
        if pk == 0:
            _products = get_products_orederd_by_price()
            category = {'name': 'Все'}
        else:
            category = get_category(pk)
            _products = get_products_in_category_orederd_by_price(pk)
        content = {
            'title': title,
            'links_menu': main_links_menu,
            'category': category,
            'products': _products,
            'categories': categories,
            'same_products': same_products,
            'hot_product': hot_product,
        }
        return render(request, 'mainapp/products.html', content)
    content = {
        'title': title, 
        'links_menu': main_links_menu, 
        'same_products': same_products,
        'categories': categories,
        'hot_product': hot_product,
    }
    return render(request, 'mainapp/catalog.html', content)


def contact(request):
    title = 'Контакты'
    content = {
            'title': title,
            'links_menu': main_links_menu,
        }
    return render(request, 'mainapp/contacts.html', content)

def product(request, pk):
    title = 'продукты'
    content = {
        'title': title,
        'links_menu': main_links_menu,
        'product_links_menu': get_categories(),
        'product': get_object_or_404(Product, pk=pk), 
    }
    
    return render(request, 'mainapp/product.html', content)

def get_categories():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        _products = cache.get(key)
        if _products is None:
            _products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
            cache.set(key, _products)
        return _products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products_orederd_by_price():
    if settings.LOW_CACHE:
        key = 'products_orederd_by_price'
        _products = cache.get(key)
        if _products is None:
            _products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
            cache.set(key, _products)
        return _products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).order_by('price')


def get_products_in_category_orederd_by_price(pk):
    if settings.LOW_CACHE:
        key = f'products_in_category_orederd_by_price_{pk}'
        _products = cache.get(key)
        if _products is None:
            _products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
            cache.set(key, _products)
        return _products
    else:
        return Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
