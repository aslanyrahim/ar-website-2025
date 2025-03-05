# services/admin.py
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Project, ProjectFeature, ProjectChallenge, TeamMember

class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 1

class ProjectChallengeInline(admin.TabularInline):
    model = ProjectChallenge
    extra = 1

@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):
    list_display = ('name', 'short_description', 'is_featured', 'order', 'status')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('is_featured', 'status')
    list_editable = ('is_featured', 'order', 'status')
    search_fields = ('name', 'short_description', 'description', 'client', 'technologies')
    summernote_fields = ('description', 'outcomes')
    inlines = [ProjectFeatureInline, ProjectChallengeInline]

@admin.register(ProjectChallenge)
class ProjectChallengeAdmin(SummernoteModelAdmin):
    list_display = ('project', 'title', 'order')
    list_filter = ('project',)
    list_editable = ('order',)
    search_fields = ('project__name', 'title', 'description', 'solution')
    summernote_fields = ('description', 'solution')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')
    filter_horizontal = ('projects',)

# You can remove these lines since we're using the @admin.register decorator
# admin.site.register(ProjectChallenge)
# admin.site.register(TeamMember)
