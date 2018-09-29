import base64

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils import timezone
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from eduflox.api import models, serializers


class AgentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AgentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Agent.objects.all()
        return models.Agent.objects.filter(user=self.request.user)

    def _send_activation_email(self, request, new_user):
        current_site = get_current_site(request)
        message = render_to_string(
            "activation.html",
            {
                "user": new_user,
                "domain": current_site.domain,
                "uid": base64.urlsafe_b64encode(new_user.pk),
                "token": default_token_generator.make_token(new_user),
            },
        )

        mail_subject = settings.EDUFLOX_ACTIVATION_EMAIL_SUBJECT
        email = EmailMessage(mail_subject, message, to=[new_user.email])
        email.send()

    def post(self, request, format=None):
        """Create new agent"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_email = serializer.data["email"]
            user = models.User.objects.create_user(
                user_email,
                email=user_email,
                first_name=serializer.data["first_name"],
                last_name=serializer.data["last_name"],
            )
            serializer.save(user=user)
            self._send_activation_email(request, user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvitationViewSet(viewsets.ModelViewSet):
    queryset = models.Invitation.objects.all()
    serializer_class = serializers.InvitationSerializer
    permission_classes = (permissions.IsAdminUser,)

    @action(methods=["post"], detail=True, permission_classes=[permissions.AllowAny])
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
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return models.School.objects.all()
        return models.School.objects.filter(created_by=self.request.user)

    def _update_status(self, school_id, status):
        """Update a school's status"""
        school = get_object_or_404(models.School, school_id)
        school.status = status
        school.save()
        return Response({"status": "School {}.".format(status)})

    @action(methods=["post"], detail=True, permission_classes=[permissions.IsAdminUser])
    def approve(self, request, pk):
        """Approve a school"""
        return self._update_status(pk, "approved")

    @action(methods=["post"], detail=True, permission_classes=[permissions.IsAdminUser])
    def reject(self, request, pk):
        """Reject a school"""
        return self._update_status(pk, "rejected")


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ServiceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return models.Service.objects.all()
        return models.Service.objects.filter(requested_by=self.request.user)


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer
    permission_classes = (permissions.IsAdminUser,)
