# notes/views.py
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics

class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer
