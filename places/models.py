from django.db import models
from django.conf import settings
from categories.models import Activity, Category

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='places')
    activities = models.ManyToManyField(Activity, blank=True, related_name='places')

    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    price_min = models.PositiveIntegerField(null=True, blank=True)
    price_max = models.PositiveIntegerField(null=True, blank=True)

    opening_hours = models.CharField(max_length=255, blank=True)
    contact_info = models.CharField(max_length=255, blank=True)

    is_verified = models.BooleanField(default=False)
    is_curated = models.BooleanField(default=False)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='owned_places')
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='places/')
    caption = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"Image for {self.place.name}"

    