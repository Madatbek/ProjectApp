from rest_framework import viewsets
from rest_framework.response import Response
from User.models import User
from .serializer import UserSerializers


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers

    def get_queryset(self):
        user = User.objects.all()
        return user
