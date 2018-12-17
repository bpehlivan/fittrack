from rest_framework import serializers

from users.models import FitUser, UserInfo


class FitUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitUser
        fields = ("username", "first_name", "last_name", "email", "password")
