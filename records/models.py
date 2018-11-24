from django.db import models


class Record(models.Model):
    user = models.ForeignKey('users.user', on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
