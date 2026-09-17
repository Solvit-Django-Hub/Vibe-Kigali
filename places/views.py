from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Place
from .serializers import PlaceSerializer


@api_view(['GET'])
def place_list(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    serializer = PlaceSerializer(place)
    return Response(serializer.data)