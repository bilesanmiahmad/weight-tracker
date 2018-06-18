from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from  tracker.models import WeightModel
from accounts.models import User
from tracker.serializers import WeightSerializer
from tracker.serializers import UserSerializer
from tracker.permissions import IsOwner

# Create your views here.


class WeightViewSet(viewsets.ModelViewSet):
    queryset = WeightModel.objects.all()
    serializer_class = WeightSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwner)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
