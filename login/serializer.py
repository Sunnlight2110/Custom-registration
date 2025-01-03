from rest_framework import serializers
from django.contrib.auth import authenticate
from registration.models import StudentModel

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    

