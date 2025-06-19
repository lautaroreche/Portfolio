from django.shortcuts import render
from .models import Project, Technology, WorkExperience, SocialMedia


def home(request):
    projects = Project.objects.all().reverse()
    technologies = Technology.objects.all()
    work_experiences = WorkExperience.objects.all()
    social_media = SocialMedia.objects.all()

    project_tags_dict = {}
    for project in projects:
        project_tags_dict[project.id] = project.tags.split(',')

    work_experience_description_dict = {}
    for work_experience in work_experiences:
        work_experience_description_dict[work_experience.id] = work_experience.description.split('.')

    return render(request, 'index.html', {
        "projects": projects,
        "project_tags_dict": project_tags_dict.items(),
        "technologies": technologies,
        "social_media": social_media,
        "work_experiences": work_experiences,
        "work_experience_description_dict": work_experience_description_dict.items(),
    })
