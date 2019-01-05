from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model, login
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from users.serializers import FitUserSerializer, PasswordResetSerializer
from users.tokens import account_activation_token

FitUser = get_user_model()


class UserRegisterViewSet(ModelViewSet):
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
                {
                    "status": "error",
                    "message": "A user with given username already exists",
                },
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
        resp_message = {
            "status": "created",
            "message": "Please check your email address to complete registering"
        }
        return Response(resp_message, status=status.HTTP_201_CREATED)


class PasswordReset(ViewSet):
    def create(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            e_mail = serializer.validated_data["e_mail"]
            try:
                user = FitUser.objects.get(e_mail=e_mail)
            except FitUser.DoesNotExist:
                resp_message = {
                    "status": "OK",
                    "message": "login info send to user with given e-mail"
                }
                return Response(resp_message, status=status.HTTP_200_OK)
            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            activation_link = "{0}/?uid={1}&token{2}".format(current_site, uid,
                                                             token)
            mail_subject = "Activate your account."
            message = "Hello {0},\n {1}".format(user.username, activation_link)
            to_email = user.email.value_to_string()
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            resp_message = {
                "status": "OK",
                "message": "login info send to user with given e-mail"
            }
            return Response(resp_message, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "fail",
                "message": "e_mail field reqired"
            }, status=status.HTTP_400_BAD_REQUEST)


class Activation(APIView):
    def get(self, request, uidb64, token):
        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user = FitUser.objects.get(pk=user_id)
        except(TypeError, ValueError, OverflowError, FitUser.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user,
                                                                     token):
            user.is_active = True
            user.save()
            login(request, user)

        resp_message = {
            "status": "activated",
            "message": "Your account is activated"
        }
        return Response(resp_message, status=status.HTTP_200_OK)


"""
TODO: Make activation view
https://stackoverflow.com/questions/50298114/django-2-how-to-register-a-user-using-email-confirmation-and-cbvs
"""
