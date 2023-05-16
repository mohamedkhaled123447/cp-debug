from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import Profile
from .serializers import profileSerializer
from .permissions import CustomPermission

# Create your views here.


class profile(ListCreateAPIView):
    permission_classes = (CustomPermission,)
    queryset = Profile.objects.all()
    serializer_class = profileSerializer

class profileDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomPermission,)
    queryset = Profile.objects.all()
    serializer_class = profileSerializer
