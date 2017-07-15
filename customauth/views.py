from rest_framework import viewsets, status, generics, mixins
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from customauth.models import MyUser
from customauth.serializer import UserSerializer, UserLoginSerializer, UserRegSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()
    permission_classes = (AllowAny,)


class ProfileView(generics.RetrieveAPIView, mixins.UpdateModelMixin):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class AuthMethod(ViewSet):
    @list_route(methods=['post'], permission_classes=[AllowAny])
    def register(self, request, **kwargs):
        serializer = UserRegSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Token.objects.get_or_create(user=user)
        return Response(status=status.HTTP_200_OK, data={"auth_token": str(user.auth_token)})

    @list_route(methods=['post'], permission_classes=[AllowAny])
    def login(self, request, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
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

    @list_route(methods=['post'], permission_classes=[AllowAny])
    def logout(self, request, **kwargs):
        request.user.auth_token.delete()

        return Response(status=status.HTTP_200_OK, data={"message": "user successfully logout"})
