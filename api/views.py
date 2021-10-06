# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(["GET"])
#@permission_classes([IsAuthenticated])
def home(request):
    data = {"username": "ishakdolek"}
    return Response(data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def home1(request):
    data = {"username": "ishakdolek"}
    return Response(data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def home2(request):
    data = {"username": "ishakdolek"}
    return Response(data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def home3(request):
    data = {"username": "ishakdolek"}
    return Response(data, status=status.HTTP_200_OK)
