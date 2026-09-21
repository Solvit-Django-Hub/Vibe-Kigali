from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

    
    
    
class Activity(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

   