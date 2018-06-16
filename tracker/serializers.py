from rest_framework import serializers
from tracker.models import WeightModel
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class WeightSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = WeightModel
        fields = ('id', 'user', 'current_weight', 'created')


