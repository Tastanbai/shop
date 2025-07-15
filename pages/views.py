from django.shortcuts import render
from .models import Certificate, PortfolioItem

# Create your views here.
def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def certificates(request):
    certificates = Certificate.objects.all()  # Получаем все сертификаты
    return render(request, 'pages/certificates.html', {'certificates': certificates})

def portfolio(request):
    items = PortfolioItem.objects.all()
    return render(request, 'pages/portfolio.html', {'items': items})