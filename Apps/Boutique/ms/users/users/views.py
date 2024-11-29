from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



@api_view(['POST'])
def login(request):

    user = get_object_or_404(User, username=request.data["username"])
    
    if not user.check_password(request.data["password"]):

        return Response (
            {
                "detail": "Not found.",
            },
            status=404
        )
    
    token, created = Token.objects.get_or_create (user=user)

    UserSerializer (instance=user)
    
    return Response(
        {
            "token": token.key,
            "user_id": user.id,
        }
    )



@api_view(['POST'])
def register(request):
    
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()
        
        user = User.objects.get(pk=serializer.data["id"])
        
        token = Token.objects.create(user=user)
        
        return Response(
            {
                "token": token.key,
                "user_id": serializer.data["id"],
            }
        )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def authenticate(request):

    return Response(
        {
            "id": request.user.id,
            "email": request.user.username,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
        },
        status=status.HTTP_200_OK
    )



@api_view(['GET'])
def auditoria(request):

    return Response(
        {
            "id": request.user.id,
            "email": request.user.username,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
        },
        status=status.HTTP_200_OK
    )