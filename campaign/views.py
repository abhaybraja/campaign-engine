from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from campaign.enums import CampaignStatus
from campaign.models import Campaign, Logs
from campaign.permissions import AdminOnly, UserOnly
from campaign.schema import CampaignPayload
from campaign.serializers import CampaignLogsSerilizer, CampaignSerilizer, LogsSerilizer
from campaign.utils import get_offset
# Create your views here.

class CampaignAPIView(APIView):
    permission_classes = [UserOnly]

    def post(self, request):
        serilizer = CampaignPayload(data=request.data)
        print(request.data)
        
        if not serilizer.is_valid():
            return Response({'detail': serilizer.errors}, status.HTTP_400_BAD_REQUEST)
        
        validated = serilizer.validated_data
        campaign = Campaign.objects.create(
            user=request.user,
            title=validated['title'],
            description=validated['description'],
            audience=validated['audience'],
            scheduled_at=validated['scheduled_at'],
        )
        
        return Response({'id': str(campaign.campaign_id)}, status.HTTP_201_CREATED)
    
    def get(self, request):
        campaigns = Campaign.objects.filter(
            user=request.user,
        ).order_by('scheduled_at')

        serializer = CampaignSerilizer(campaigns, many=True)
        return Response(serializer.data)
    
    def delete(self, request):
        campaign = Campaign.objects.filter(
            user=request.user,
        ).first()

        if not campaign:
            return Response({'detail': "Campaign not found"}, status.HTTP_400_BAD_REQUEST)

        if campaign.status != CampaignStatus.PENDING:
            return Response({'detail': "You cannot delete trigerred/failed campaign!"}, status.HTTP_400_BAD_REQUEST)
        
        campaign.delete()
        return Response({'detail': "Deleted successfully!"})
    
    def put(self, request):
        campaign = Campaign.objects.filter(
            user=request.user,
        ).first()

        if not campaign:
            return Response({'detail': "Campaign not found"}, status.HTTP_400_BAD_REQUEST)

        if campaign.status == CampaignStatus.TRIGERRED:
            return Response({'detail': "You cannot update trigerred campaign!"}, status.HTTP_400_BAD_REQUEST)
        
        serilizer = CampaignPayload(data=request.data, partial=True)
        
        if not serilizer.is_valid():
            return Response({'detail': serilizer.errors}, status.HTTP_400_BAD_REQUEST)
        
        validated = serilizer.validated_data

        if validated.get('title'):
            campaign.title = validated['title']
        if validated.get('description'):
            campaign.description = validated['description']
        if validated.get('audience'):
            campaign.audience = validated['audience']
        if validated.get('scheduled_at'):
            campaign.scheduled_at = validated['scheduled_at']
            campaign.status = CampaignStatus.PENDING

        campaign.save()
        return Response({'detail': "Updated successfully!"})



class AllCampaignAPIView(APIView):
    permission_classes = [AdminOnly]

    def get(self, request):
        _from, _to = get_offset(request.GET, 15)
        campaigns = (
            Campaign.objects.all()
            .prefetch_related('logs')
            .order_by('scheduled_at')[_from:_to]
        )

        serializer = CampaignLogsSerilizer(campaigns, many=True)
        return Response(serializer.data)


class CampaignLogsAPIView(APIView):
    permission_classes = [UserOnly]

    def get(self, request):
        id = request.GET.get('campaign_id')

        if not id:
            return Response({'details': "Campaign Id required"}, status.HTTP_400_BAD_REQUEST)
    
        logs = Logs.objects.filter(campaign__campaign_id=id).order_by('created_at')

        serializer = LogsSerilizer(logs, many=True)
        return Response(serializer.data)


class FailedTriggersAPIView(APIView):
    permission_classes = [AdminOnly]

    def get(self, request):

        campaigns = Campaign.objects.filter(
            status=CampaignStatus.FAILED
        ).order_by('updated_at')

        serializer = CampaignSerilizer(campaigns, many=True)
        return Response(serializer.data)
