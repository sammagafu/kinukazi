from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import serializers
from . models import Accounts
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['email'] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=Accounts.objects.all())])
    phone_number = serializers.CharField(required=True,validators=[UniqueValidator(queryset=Accounts.objects.all())])
    password = serializers.CharField(write_only=True, validators=[validate_password],style={'input_type': 'password'})

    class Meta:
        model = Accounts
        fields = "__all__"

    def create(self, validated_data):
        user = Accounts.objects.create_user(validated_data['email'], 
        validated_data['password']
        )
        user.phone_number = validated_data['phone_number']
        user.avatar = validated_data['avatar']
        return user


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        exclude = ('password','email')

class AccountsProfile(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        exclude = ('password',)
        read_only_fields = ["email","memberId"]

class UpdateProfileImage(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['avatar']