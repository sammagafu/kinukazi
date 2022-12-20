# from .serializer import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer,UpdateProfileImage,MyTokenObtainPairSerializer,AccountsProfile
from . models import Accounts
from rest_framework import generics


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = Accounts.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class Users(generics.ListAPIView):
    queryset = Accounts.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UsersDetail(generics.RetrieveDestroyAPIView):
    queryset = Accounts.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    lookup_field = "memberId"

class UserProfile(generics.RetrieveUpdateAPIView):
    queryset = Accounts.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountsProfile

    def get_object(self):
        obj = get_object_or_404(Accounts, pk=self.request.user.id)
        return obj
class UpdateUserProfilePicture(generics.RetrieveUpdateAPIView):
    queryset = Accounts.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateProfileImage

    def get_object(self):
        obj = get_object_or_404(Accounts, pk=self.request.user.id)
        return obj