# blog/admin.py
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_at', 'is_featured')
    list_filter = ('status', 'created_at', 'category', 'is_featured')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('author',)
    list_editable = ('status', 'is_featured')
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'author', 'category', 'tags', 'content')
        }),
        ('Featured Image', {
            'fields': ('featured_image',)
        }),
        ('Summary', {
            'fields': ('excerpt',)
        }),
        ('Meta', {
            'fields': ('status', 'is_featured', 'published_at')
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description'),
            'classes': ('collapse',)
        }),
    )
