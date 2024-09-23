
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User

@api_view(['POST'])
def login_view(request):
    phone = request.data.get('phone')
    password = request.data.get('password')

    user = authenticate(request, username=phone, password=password)

    if user is not None:
        login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid phone or password"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signup_view(request):
    name = request.data.get('name')
    email = request.data.get('email')
    phone = request.data.get('phone')
    password = request.data.get('password')

    if User.objects.filter(username=phone).exists():
        return Response({"error": "Phone number already registered."}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=phone, password=password, email=email, first_name=name)
    user.save()

    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)