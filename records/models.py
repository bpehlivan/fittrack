from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()

    class Meta:
        unique_together = ("user", "date")
        index_together = ("user", "date")

    def __str__(self):
        return "user:{0}-date:{1}".format(self.user, self.date)
