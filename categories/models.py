from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(unique=True)

    
    
    
class Activity(models.Model):
    name = models.CharField(max_length=100)

   