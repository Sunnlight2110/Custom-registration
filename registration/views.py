from django.shortcuts import render
from .serializer import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  

class StudentView(APIView):

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        

        if serializer.is_valid():
            # This will call the `create` method inside the serializer, saving the data to the DB
            serializer.save()
            
            # Return a response with the serialized data and status code 201 Created
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
        # If the data is invalid, return a 400 Bad Request response with the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
