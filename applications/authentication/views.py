from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from applications.authentication.middleware import login_user
from applications.authentication.serializers import UserCreateSerializer


class RegistrationViewSet(ViewSet):
    @permission_classes([AllowAny])
    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @permission_classes([AllowAny])
    @action(detail=False, methods=['post'])
    def login(self, request):
        data = login_user(request.data.get('username'),
                          request.data.get('password'))

        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
