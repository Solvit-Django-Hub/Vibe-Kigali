from django.db import models
from django.conf import settings
from places.models import Place

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Image for {self.place.name}"

    class Meta:
        unique_together = ('user', 'place')

    def __str__(self):
        return f"{self.user.username} ❤ {self.place.name}"