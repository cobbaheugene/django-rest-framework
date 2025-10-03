from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializers

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    "api endpoint that allows users to be viewed or edited"
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    'api endpoint that allows groups to be viewed or edited'
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]