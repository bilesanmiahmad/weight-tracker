from rest_framework import serializers
from tracker.models import WeightModel


class WeightSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()

    class Meta:
        model = WeightModel
        fields = ('id', 'current_weight', 'created')
