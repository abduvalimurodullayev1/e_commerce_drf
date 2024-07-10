from rest_framework import serializers
from app.models import MyFavourites


class MyFavoriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MyFavourites
        fields = ['product', 'user']  # Include 'user' instead of 'user_id'
