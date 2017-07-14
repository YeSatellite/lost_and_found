from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from customauth.models import MyUser
from customauth.serializer import UserSerializer, UserRegSerializer, LoginSerializer


class UserViewSet(GenericViewSet):
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()
    permission_classes = (AllowAny,)

    @list_route(methods=['post'], permission_classes=[AllowAny])
    def register(self, request, **kwargs):
        serializer = UserRegSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Token.objects.get_or_create(user=user)
        return Response(status=status.HTTP_200_OK, data={"auth_token": str(user.auth_token)})

    @list_route(methods=['post'], permission_classes=[AllowAny])
    def login(self, request, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = {
            'username': serializer.validated_data['username'],
            'password': serializer.validated_data['password']
        }
        serializer = AuthTokenSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        Token.objects.get_or_create(user=user)

        return Response(status=status.HTTP_200_OK, data={"auth_token": str(user.auth_token)})
