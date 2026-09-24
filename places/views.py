from rest_framework import generics, permissions
from core.permissions import IsOwnerOrReadOnly
from .models import Place
from .serializers import PlaceSerializer

class PlaceListCreateView(generics.ListCreateAPIView):
    queryset = Place.objects.select_related('category').prefetch_related('activities', 'images')
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.select_related('category').prefetch_related('activities', 'images')
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
