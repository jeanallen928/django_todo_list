from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "name", "gender", "age", "introduction")
        read_only_fields = ["email",]
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
        }

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.name = validated_data.get("name", instance.name)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.age = validated_data.get("age", instance.age)
        instance.introduction = validated_data.get(
            "introduction", instance.introduction)
        instance.password = validated_data.get("password", instance.password)
        instance.set_password(instance.password)
        instance.save()
        return instance


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['name'] = user.name
        token['gender'] = user.gender
        token['age'] = user.age
        return token
