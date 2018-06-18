from rest_framework import serializers
from tracker.models import WeightModel

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')


class WeightSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = WeightModel
        fields = ('id', 'user', 'current_weight', 'created')


