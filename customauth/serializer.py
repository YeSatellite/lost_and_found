from rest_framework import serializers

from customauth.models import MyUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'date_of_birth')
        read_only_fields = ('id', 'username', 'email')


class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = MyUser(**validated_data)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20, required=True)
    password = serializers.CharField(max_length=20, required=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

