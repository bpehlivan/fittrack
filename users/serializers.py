from rest_framework import serializers

from users.models import FitUser


class FitUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitUser
        fields = ("username", "first_name", "last_name", "email", "password")


class PasswordResetSerializer(serializers.Serializer):
    e_mail = serializers.EmailField()

