# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap, CategorySitemap
from main.sitemaps import StaticViewSiteMap
from projects.sitemaps import ProjectSitemap
from services.sitemaps import ServiceSitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'static': StaticViewSiteMap,
    'posts': PostSitemap,
    'categories': CategorySitemap,
    'projects': ProjectSitemap,
    'services': ServiceSitemap,
}

urlpatterns = [
    path('', include(('main.urls', 'main'), namespace='main')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('services/', include(('services.urls', 'services'), namespace='services')),
    path('projects/', include(('projects.urls', 'projects'), namespace='projects')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("__reload__/", include("django_browser_reload.urls")),
]



# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)