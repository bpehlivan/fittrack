from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from enumfields import EnumField

from users.enums import Measurement


class FitUser(AbstractUser):
    register_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=False)
    last_modified_date = models.DateTimeField(auto_now=True)
    email = models.EmailField(_('email address'), max_length=200,
                              help_text='required', null=False)

    def __str__(self):
        return self.username


class UserInfo(models.Model):
    user = models.ForeignKey(FitUser, on_delete=models.CASCADE)
    unit_type = EnumField(Measurement, default=Measurement.METRIC)
    height = models.FloatField()
