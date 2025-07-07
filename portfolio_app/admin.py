from django.contrib import admin
from .models import Project, Technology, WorkExperience, SocialMedia
from django.contrib.sessions.models import Session


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary', 'tags', 'image', 'repo_url', 'order')
    search_fields = ('id', 'title', 'summary', 'tags', 'image', 'repo_url', 'order')


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'order')
    search_fields = ('id', 'name', 'image', 'order')


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'location', 'start_date', 'end_date', 'image', 'description', 'order')
    search_fields = ('id', 'title', 'company', 'location', 'start_date', 'end_date', 'image', 'description', 'order')


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'hyperlink', 'order')
    search_fields = ('id', 'name', 'image', 'hyperlink', 'order')


admin.site.register(Session)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
