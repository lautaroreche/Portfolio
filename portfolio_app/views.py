from django.shortcuts import render
from .models import Project, Technology, WorkExperience, SocialMedia
import json


def get_project_images(projects):
    images_json = {}
    for project in projects:
        image_urls = [project.image.url]
        for image_field in ['image2']:
            image = getattr(project, image_field)
            if image:
                image_urls.append(image.url)
        images_json[project.id] = json.dumps(image_urls)
    return images_json


def home(request):
    projects = Project.objects.all()
    technologies = Technology.objects.all()
    work_experiences = WorkExperience.objects.all()
    social_media = SocialMedia.objects.all()

    work_experience_description_dict = {}
    for work_experience in work_experiences:
        work_experience_description_dict[work_experience.id] = work_experience.description.split('.')

    context = {
        "projects": projects,
        "images_json": get_project_images(projects),
        "technologies": technologies,
        "social_media": social_media,
        "work_experiences": work_experiences,
        "work_experience_description_dict": work_experience_description_dict.items(),
    }
    
    return render(request, 'index.html', context)
