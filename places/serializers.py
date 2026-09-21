from rest_framework import serializers
from .models import Place, PlaceImage
from categories.serializers import CategorySerializer, ActivitySerializer
from categories.models import Category, Activity

class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ['id', 'image', 'caption']

class PlaceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    activities = ActivitySerializer(many=True, read_only=True)
    images = PlaceImageSerializer(many=True, read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    activity_ids = serializers.PrimaryKeyRelatedField(
        queryset=Activity.objects.all(), source='activities', many=True, write_only=True, required=False
    )

    class Meta:
        model = Place
        fields = [
            'id', 'name', 'description', 'category', 'category_id',
            'activities', 'activity_ids', 'images', 'address',
            'latitude', 'longitude', 'price_min', 'price_max',
            'opening_hours', 'contact_info', 'is_verified', 'is_curated',
            'owner', 'created_at',
        ]
        read_only_fields = ['owner', 'is_verified', 'is_curated', 'created_at']