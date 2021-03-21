from django.shortcuts import render
from rest_framework import generics
from .serializers import AccountSerializer
from django.contrib.auth.models import User


class RegisterView(generics.ListCreateAPIView):
    queryset  = User.objects.all()
    serializer_class = AccountSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer

