from rest_framework.serializers import ModelSerializer

from records.models import Record


class RecordSerializer(ModelSerializer):
    class Meta:
        model = Record
        fields = ["date", "weight"]