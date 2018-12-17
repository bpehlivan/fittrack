from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from users.serializers import FitUserSerializer
from users.models import FitUser
from users.tokens import account_activation_token


class UserViewSet(ModelViewSet):
    serializer_class = FitUserSerializer
    queryset = FitUser.objects.all()
    renderer_classes = [JSONRenderer]
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serialized_data = self.get_serializer(request.data)
        serialized_data.is_valid(raise_exceptions=True)
        validated_data = serialized_data.validated_data
        if FitUser.objects.does_user_exists(validated_data["username"]):
            return Response(
                {"error": "A user with given username already exists"},
                status=status.HTTP_409_CONFLICT)
        user_password = validated_data.pop("password")
        user = FitUser(**validated_data)
        user.set_password(user_password)
        user.is_active = False

        mail_subject = "Activate your account."
        current_site = get_current_site(request)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)
        activation_link = "{0}/?uid={1}&token{2}".format(current_site, uid,
                                                         token)
        message = "Hello {0},\n {1}".format(user.username, activation_link)
        to_email = user.email.value_to_string()

        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        resp_message = "Please check your email address" \
                       " to complete the registration."
        return Response({
            "created": resp_message}, status=status.HTTP_201_CREATED)


"""
TODO: Make activation view
"""
