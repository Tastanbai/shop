from django.contrib import admin
from .models import Certificate, PortfolioItem

admin.site.register(PortfolioItem)
admin.site.register(Certificate)
