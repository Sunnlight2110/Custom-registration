from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import LoginSerializer
from rest_framework.response import Response
from registration.models import StudentModel
from django.contrib.auth import authenticate


class LoginView(APIView):
    def post(self, request):
        print(request.data,"------")
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                         
                user = authenticate(request, email=email, password=password)
                refresh = RefreshToken.for_user(user)

                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                    'user': {
                        'id': user.id,
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                    },
                }, status=status.HTTP_200_OK)
            except Exception as a:
                print(a)
                return Response(
                    {"massage":"invalid email of password"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
