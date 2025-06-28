from celery import shared_task
from django.utils import timezone
from campaign.enums import CampaignStatus, LogsStatus
from campaign.handlers import handle_campaign_trigerred
from campaign.models import Campaign, Logs

@shared_task
def check_tigger_campaigns():
    print(timezone.localtime())
    campaigns = Campaign.objects.filter(
        scheduled_at__lte=timezone.localtime(), status=CampaignStatus.PENDING
    )

    for campaign in campaigns:
        try:
            campaign.status = CampaignStatus.TRIGERRED
            campaign.save()


            Logs.objects.create(
                campaign=campaign,
                status=LogsStatus.SUCCSESS,
                message="Triggered with "+campaign.channel
            )
            handle_campaign_trigerred(campaign)

            Logs.objects.create(
                campaign=campaign,
                status=LogsStatus.SUCCSESS,
                message="Executed scuccessfully"
            )

            campaign.status = CampaignStatus.EXEC
            campaign.save()
        except Exception as e:
            print("campaign update T -----", campaign, e)
            campaign.status = CampaignStatus.FAILED
            campaign.save()
            Logs.objects.create(
                campaign=campaign,
                status=LogsStatus.FAILED,
                error=str(e)[:255]
            )
