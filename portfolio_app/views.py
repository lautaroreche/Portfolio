from django.shortcuts import render
from .models import Project, Technology, WorkExperience, SocialMedia


def home(request):
    projects = Project.objects.filter(type__in=['frontend', 'backend'])
    technologies = Technology.objects.all()
    work_experiences = WorkExperience.objects.all()
    social_media = SocialMedia.objects.all()

    work_experience_description_dict = {}
    for work_experience in work_experiences:
        work_experience_description_dict[work_experience.id] = work_experience.description.split('.')

    context = {
        "projects": projects,
        "technologies": technologies,
        "social_media": social_media,
        "work_experiences": work_experiences,
        "work_experience_description_dict": work_experience_description_dict.items(),
    }
    
    return render(request, 'index.html', context)


def web(requests):
    projects = Project.objects.filter(type__in=['frontend', 'web-portfolio'])
    context = {
        "projects": projects,
    }
    return render(requests, 'web.html', context)
