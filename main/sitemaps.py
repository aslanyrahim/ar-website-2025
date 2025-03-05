from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSiteMap(Sitemap):
    def items(self):
        return ["main:home", "main:about", "contact:contact_form",]
    
    def location(self, obj):
        return reverse(obj)