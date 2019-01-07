from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer, HTMLFormRenderer

from users.serializers import UserSerializer, UserCreationSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    renderer_classes = [JSONRenderer, HTMLFormRenderer]

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreationSerializer
        return UserSerializer

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        User.objects.create_user(**validated_data)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_active = False
