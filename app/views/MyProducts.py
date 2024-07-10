from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from app.models import MyFavourites
from app.permssions_1 import IsAuthorOrReadOnly
from app.serializers.MyProducts import MyFavoriteSerializer


class MyFavoriteCreate(CreateAPIView):
    serializer_class = MyFavoriteSerializer
    queryset = MyFavourites.objects.all()
    permission_classes = [IsAuthenticated]


class MyFavoriteView(ListAPIView):
    serializer_class = MyFavoriteSerializer
    queryset = MyFavourites.objects.all()
    permission_classes = [IsAuthorOrReadOnly]