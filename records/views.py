from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from records.models import Record
from records.serializers import RecordSerializer

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class RecordViewSet(ModelViewSet):
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Record.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        Record.objects.create(user=self.request.user, **validated_data)

    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        response = super().list(self, request, *args, **kwargs)
        return response
