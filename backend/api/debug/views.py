from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import Profile
from .serializers import profileSerializer
from .permissions import CustomPermission

# Create your views here.


class profileViewSet(ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Profile.objects.all()
    serializer_class = profileSerializer