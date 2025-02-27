from rest_framework import serializers
from UserApp.models import ModelUser, ModelAddress
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ModelUser
        fields = ("username", "first_name", "last_name")


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=ModelUser.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = ModelUser
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', "avatar", "isCustomer")
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = ModelUser.objects.create(
            username   = validated_data['username'],
            email      = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name  = validated_data['last_name'],
            avatar     = validated_data.get("avatar"), # maybe blank cuz not required fields
            isCustomer = validated_data.get("isCustomer")
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=ModelAddress
        fields=("unique_id","name","city","street","address")


class DeleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ModelUser
        fields = ("username",)