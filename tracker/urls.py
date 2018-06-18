from django.urls import path, include
from rest_framework import routers

from tracker.views import WeightViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('tracker', WeightViewSet, 'tracker')
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
