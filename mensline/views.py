from django.shortcuts import render
from slider.models import Slider
from store.models import Product

def home(request):
    slider_list = Slider.objects.all()

    # Просто берем все доступные товары
    most_popular_products = Product.objects.filter(is_available=True)

    context = {
        'slider_list': slider_list,
        'most_popular_products': most_popular_products,
    }

    return render(request, 'home.html', context)


