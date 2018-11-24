from django.db import models
from django.contrib.auth.models import User
from enumfields import EnumField

from users.enums import Measurement


class FitUser(User):
    township = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    register_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True)
    height = EnumField(Measurement, default=Measurement.METRIC)

    def __str(self):
        return self.username

