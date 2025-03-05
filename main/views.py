# main/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post
from services.models import Service
from projects.models import Project

class HomeView(TemplateView):
    template_name = 'main/home.html'
    #template_name = 'test_home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_posts'] = Post.objects.filter(status='published', is_featured=True)[:3]
        context['recent_posts'] = Post.objects.filter(status='published').order_by('-published_at')[:3]
        context['featured_services'] = Service.objects.filter(is_featured=True)[:3]
        context['featured_projects'] = Project.objects.filter(is_featured=True)[:3]
        return context

class AboutView(TemplateView):
    template_name = 'main/about.html'

