from django.contrib import admin

from django.contrib import admin
from .models import Place, PlaceImage

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_min', 'price_max', 'is_verified', 'is_curated')
    inlines = [PlaceImageInline]