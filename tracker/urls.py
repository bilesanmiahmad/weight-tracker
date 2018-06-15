from django.urls import path, include
from rest_framework import routers

from tracker.views import WeightViewSet

router = routers.DefaultRouter()
router.register('tracker', WeightViewSet)

urlpatterns = [
    path('', include(router.urls))
]
