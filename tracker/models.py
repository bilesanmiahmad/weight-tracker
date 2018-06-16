from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class WeightModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='weights'
    )
    current_weight = models.IntegerField()
    created = models.DateTimeField(
        auto_now_add=True
    )
