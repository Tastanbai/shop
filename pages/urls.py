from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('certificates/', views.certificates, name='certificates'),
    path('portfolio/', views.portfolio, name='portfolio'),
]