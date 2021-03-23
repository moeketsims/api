from django.shortcuts import render
from .models import Upload
from .serializers import UplodSerializer
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.


class UploadView(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UplodSerializer




""" class UploadView(ListCreateAPIView):
    serializer_class = UplodSerializer

    def perform_create(self, request):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Upload.objects.filter(owner=self.request.user)

class DetailsView(RetrieveUpdateDestroyAPIView):

    lookup_field = 'id'
    
    def get_queryset(self):
        return Upload.objects.filter(owner=self.request.user) """