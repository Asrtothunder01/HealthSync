from django.contrib.auth import authenticate

from .serializers import UserSerializer

from rest_framework import status

from rest_framework.generics import CreateAPIView

from rest_framework.response import Response

from .models import CustomUser

# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class = UserSerializer
    
    
    def post (self,request):

        data = request.data

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(CreateAPIView):
    serializer_class = UserSerializer

    def post(self,request):
        username = request.data.get('username')

        password = request.data.get('password')

        user = authenticate(username=username,password=password)

        if user:
            return Response({'message':'Login successful!'},status = status.HTTP_200_OK)
        return Response({'error':"Invalid credentials"},status = status.HTTP_400_BAD_REQUEST)

        



