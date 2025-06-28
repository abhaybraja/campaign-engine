from django.db import models
from django.conf import settings
import uuid

from campaign.enums import CampaignChannel, CampaignStatus, LogsStatus

# Create your models here.

class Campaign(models.Model):
    campaign_id = models.UUIDField(default=uuid.uuid4, db_index=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        related_name="campaigns"
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    audience = models.TextField()
    scheduled_at = models.DateTimeField()
    channel = models.CharField(max_length=10, choices=CampaignChannel.CHOICES, default=CampaignChannel.EMAIL)
    status = models.CharField(max_length=12, choices=CampaignStatus.CHOICES, default=CampaignStatus.PENDING) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Logs(models.Model):
    campaign = models.ForeignKey(Campaign, models.CASCADE, related_name='logs')
    status = models.CharField(max_length=12, choices=LogsStatus.CHOICES)
    message = models.CharField(max_length=255, null=True)
    error = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)