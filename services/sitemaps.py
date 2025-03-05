# services/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Service

class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7
    
    def items(self):
        return Service.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at