# services/admin.py
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Service, ServiceFeature

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1

@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):
    list_display = ('name', 'short_description', 'is_featured', 'order')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_featured',)
    list_editable = ('is_featured', 'order')
    search_fields = ('name', 'short_description', 'description')
    summernote_fields = ('description',)
    inlines = [ServiceFeatureInline]
