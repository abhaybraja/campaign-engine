
from rest_framework import serializers

from campaign.models import Campaign, Logs

class LogsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = '__all__'

class CampaignLogsSerilizer(serializers.ModelSerializer):
    logs = LogsSerilizer(many=True)
    class Meta:
        model = Campaign
        fields = '__all__'


class CampaignSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
