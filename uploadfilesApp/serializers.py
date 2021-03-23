from rest_framework import serializers
from .models import Upload

class UplodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'