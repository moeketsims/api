from rest_framework import serializers
from django.contrib.auth.models import User

class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email     = serializers.EmailField()
    password  = serializers.CharField(max_length=30, min_length=6, write_only=True)

    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)