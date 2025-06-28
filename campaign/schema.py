from django.utils import timezone
from rest_framework import serializers

class CampaignPayload(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
    audience = serializers.CharField(max_length=10000)
    scheduled_at = serializers.DateTimeField()

    def validate_scheduled_at(self, value):
        if value and value <= timezone.now():
            raise serializers.ValidationError('scheduled_at should be future datettime!')
        return value