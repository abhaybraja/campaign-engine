from django.shortcuts import render
from rest_framework import generics, views, response
from rest_framework.permissions import AllowAny
from users.models import User
from users.serializers import RegisterSerializer

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    serializer_class = RegisterSerializer


class HealthView(views.APIView):
    def get(self, request):
        return response.Response({'status': 'ok'})