from django.db import models
from cloudinary.models import CloudinaryField


class Project(models.Model):
    TYPE_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('web-portfolio', 'Web portfolio'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=250)
    tags = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='frontend')
    public_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    image = CloudinaryField('image', resource_type='image', blank=True, null=True)
    image2 = CloudinaryField('image2', resource_type='image', blank=True, null=True)
    image3 = CloudinaryField('image3', resource_type='image', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_tags(self):
        return [tag.strip() for tag in self.tags.split(",") if tag.strip()]
    
    class Meta:
        ordering = ['order']
    

class Technology(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = CloudinaryField('image', resource_type='image')
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']
    

class SocialMedia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    hyperlink = models.CharField(max_length=100)
    image = CloudinaryField('image', resource_type='image')
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']

    
class WorkExperience(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    image = CloudinaryField('image', resource_type='image')
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']
