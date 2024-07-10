from tokenize import TokenError

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from app.models import User


class RegisterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "phone_number", 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        hashed_password = make_password(password)
        user = User.objects.create(**validated_data,
                                   password=hashed_password)
        return user


class LoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=20)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["phone_number", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):

        phone_number = data.get("phone_number")
        password = data.get("password")

        if phone_number and password:
            user = authenticate(username=phone_number, password=password)
            if not user:
                raise serializers.ValidationError("Noto'g'ri ma'lumotlar")
        else:
            raise serializers.ValidationError("Telefon raqami va parol ham talab qilinadi")

        data['profile'] = user
        return data



class LogoutModelSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, data):
        self.token = data['refresh_token']
        return data

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            raise serializers.ValidationError(
                'Token is expired or invalid'
            )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'image']
        extra_kwargs = {
            'phone_number': {'read_only': True}
        }
