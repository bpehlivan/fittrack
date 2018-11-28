from django.db import models
from django.contrib.auth.models import User
from enumfields import EnumField

from users.enums import Measurement


class FitUser(User):
    register_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(_('active'), default=False)

    def __str__(self):
        return self.username


class UserInfo(models.Model):
    user = models.ForeignKey(FitUser, on_delete=models.CASCADE)
    unit_type = EnumField(Measurement, default=Measurement.METRIC)
    height = models.FloatField()
