from django.db import models
from django.contrib.auth.models import User
from enumfields import EnumField

from users.enums import Measurement


class FitUser(User):
    register_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True)
    height = EnumField(Measurement, default=Measurement.METRIC)
    is_active = models.BooleanField(_('active'), default=False)

    def __str(self):
        return self.username

