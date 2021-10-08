# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permissions import IsEditor, IsAdmin
from .serializers import PostSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def home(request):
    data = {"username": "ishakdolek"}
    return Response(data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def home1(request):
    data = {"username": "ishakdolek"}
    return Response(data, status=status.HTTP_200_OK)


@swagger_auto_schema(methods=['POST'], request_body=PostSerializer)
@api_view(["POST"])
@permission_classes([IsAuthenticated, IsEditor])  # Add custom permission
def home2(request):
    data = {"username": "ishakdolek"}
    return Response(data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsAdmin])  # Just admin can delete items.
def home3(request):
    data = {"username": "ishakdolek"}
    return Response(data, status=status.HTTP_200_OK)
