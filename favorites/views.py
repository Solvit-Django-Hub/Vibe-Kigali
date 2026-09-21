from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Favorite
from .serializers import FavoriteSerializer


@api_view(['GET'])
def favorite_list(request):
    favorites = Favorite.objects.all()
    serializer = FavoriteSerializer(favorites, many=True)
    return Response(serializer.data)
