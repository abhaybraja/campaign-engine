from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from users.models import User
from users.serializers import RegisterSerializer

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    serializer_class = RegisterSerializer