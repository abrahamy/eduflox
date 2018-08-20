from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from eduflox.api import models, serializers


class AgentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AgentSerializer

    def get_queryset(self):
        if not self.request.user.is_staff:
            return models.Agent.objects.filter(user=self.request.user)
        return models.Agent.objects.all()


class InvitationViewSet(viewsets.ModelViewSet):
    queryset = models.Invitation.objects.all()
    serializer_class = serializers.InvitationSerializer

    def get_permissions(self):
        if self.action == "accept":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]

    @action(methods=[], detail=True)
    def accept(self, request, token=None):
        # Accept invitation if it has not lapsed else return 404
        seven_days_ago = timezone.now() - timezone.timedelta(days=7)
        invitation = get_object_or_404(
            models.Invitation, token=token, created_at__lt=seven_days_ago
        )
        invitation.accept()
        return Response({"status": "Invitation accepted."})


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SchoolSerializer

    def get_queryset(self):
        if not self.request.user.is_staff:
            return models.School.objects.all()
        return models.School.objects.filter(created_by=self.request.user)


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ServiceSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Service.objects.all()
        return models.Service.objects.filter(requested_by=self.request.user)


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer
    permission_classes = (permissions.IsAdminUser,)
