from django.urls import path

from campaign.views import AllCampaignAPIView, CampaignAPIView, CampaignLogsAPIView, FailedTriggersAPIView

urlpatterns = [
    path('campaign', CampaignAPIView.as_view(), name='campaign'),
    path('campaign/all', AllCampaignAPIView.as_view(), name='admin-campaigns'), # for admin only
    path('campaign/logs', CampaignLogsAPIView.as_view(), name='campaign logs'),
    path('campaign/failed', FailedTriggersAPIView.as_view(), name='campaigns failed'), # for admin only
]