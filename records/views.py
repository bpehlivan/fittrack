from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from records.models import Record
from records.serializers import RecordSerializer


class RecordViewSet(ModelViewSet):
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Record.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        Record.objects.create(user=self.request.user, **validated_data)
