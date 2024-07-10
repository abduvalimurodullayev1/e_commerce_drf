from rest_framework.generics import GenericAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from app.models import User
from app.serializers.user_auth import LoginSerializer, RegisterModelSerializer, LogoutModelSerializer, ProfileSerializer


class UserRegisterView(APIView):
    @swagger_auto_schema(
        request_body=RegisterModelSerializer,
        responses={
            status.HTTP_201_CREATED: "Ro'yxatdan ot'ingiz",
            status.HTTP_400_BAD_REQUEST: "Xato ma'lumotlar",
        }
    )
    def post(self, request):
        serializer = RegisterModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"Message": "Ro'yxatdan ot'ingiz"},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            status.HTTP_200_OK: "Siz tizimga kirdingiz",
            status.HTTP_400_BAD_REQUEST: "Noto'g'ri ma'lumotlar",
        }
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['profile']
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            # token, created = Token.objects.get_or_create(profile=profile)
            return Response(data={"Message": "Siz tizimga kirdingiz",
                                  # "token":token.key
                                  'access_token': access_token,
                                  'refresh_token': refresh_token},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Noto'g'ri ma'lumotlar"},
                            status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(GenericAPIView):
    serializer_class = LogoutModelSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={'message': 'Siz muvaffaqiyatli tizimdan  chiqdingiz.'},
            status=status.HTTP_204_NO_CONTENT)


class UpdateProfileApiView(UpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def get_object(self):
        user = self.request.user
        return user


class ProfileRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def get_object(self):
        user = self.request.user
        return user
