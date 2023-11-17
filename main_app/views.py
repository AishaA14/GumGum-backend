import os # environ variables
import uuid # unique id for each image
import boto3 # amazon bucket for the images
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]