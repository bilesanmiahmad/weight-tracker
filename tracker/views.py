from django.shortcuts import render
from rest_framework import viewsets
from  tracker.models import WeightModel
from tracker.serializers import WeightSerializer

# Create your views here.


class WeightViewSet(viewsets.ModelViewSet):
    queryset = WeightModel.objects.all()
    serializer_class = WeightSerializer
