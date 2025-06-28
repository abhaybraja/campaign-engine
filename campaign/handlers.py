from campaign.enums import CampaignChannel
from campaign.models import Campaign
import time

def handle_campaign_trigerred(campaign: Campaign):
    if campaign.channel == CampaignChannel.EMAIL:
        # Send email to provideed audience
        time.sleep(100)
    elif campaign.channel == CampaignChannel.WHATSAPP:
        # Send whatsapp message to provideed audience
        time.sleep(100)
    else:
        print("Invalid channel")