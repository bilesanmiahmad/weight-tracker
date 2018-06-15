from django.db import models

# Create your models here.


class WeightModel(models.Model):
    current_weight = models.IntegerField()
    created = models.DateTimeField(
        auto_now_add=True
    )
