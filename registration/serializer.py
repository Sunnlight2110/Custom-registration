from .models import StudentModel
from rest_framework import serializers
from django.contrib.auth.hashers import make_password,check_password



class StudentSerializer(serializers.ModelSerializer):  
    class Meta:
        model = StudentModel
        fields = '__all__'  

    

    def create(self, validated_data):
        password = validated_data.get('password')
        validated_data['password'] = make_password(password)  
        
        return StudentModel.objects.create(**validated_data)