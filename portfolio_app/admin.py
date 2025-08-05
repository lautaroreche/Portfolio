from django.contrib import admin
from .models import Project, Technology, WorkExperience, SocialMedia
from django.contrib.sessions.models import Session


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tags', 'type', 'repo_url', 'order')
    search_fields = ('title', 'summary', 'tags', 'type', 'repo_url')


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')
    search_fields = ('name',)


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'location', 'start_date', 'end_date', 'description', 'order')
    search_fields = ('title', 'company', 'location', 'description')


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hyperlink', 'order')
    search_fields = ('name', 'hyperlink')


admin.site.register(Session)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
