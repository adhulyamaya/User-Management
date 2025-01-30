from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import (api_view,renderer_classes,permission_classes,)
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from main.functions import get_user_token
from main_admin.models import MainAdmin, Staff, CustomUser


@api_view(["POST"])
@permission_classes([AllowAny])
def main_admin_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    # Validate input
    if not username or not password:
        return Response({
            "StatusCode": 6001,
            "message": "Username and password required"
        }, status=status.HTTP_400_BAD_REQUEST)

    # Get user and validate existence
    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return Response({
            "StatusCode": 6001,
            "message": "User not found"
        }, status=status.HTTP_404_NOT_FOUND)

    # Check if user is main admin
    if not user.groups.filter(name='main_admin').exists():
        return Response({
            "StatusCode": 6001,
            "message": "Unauthorized access"
        }, status=status.HTTP_403_FORBIDDEN)

    # Get token
    try:
        token_response = get_user_token(request, user.user_id, password)
        if token_response.status_code != 200:
            return Response({
                "StatusCode": 6001,
                "message": "Invalid credentials"
            }, status=status.HTTP_401_UNAUTHORIZED)

        # Get admin details
        main_admin = get_object_or_404(MainAdmin, user=user)
        
        return Response({
            "StatusCode": 6000,
            "token": token_response.json(),
            "message": "Login successful",
            "user_type": "main_admin",
            "name": main_admin.name
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "StatusCode": 6001,
            "message": f"Login failed: {str(e)}"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
