from django.db import models
from django.contrib.auth.models import User
from enumfields import EnumField

from users.enums import Measurement


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unit_type = EnumField(Measurement, default=Measurement.METRIC)
    height = models.FloatField()
