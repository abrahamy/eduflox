import rest_framework.serializers as serializers
import eduflox.api.models as models


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agent


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invitation


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.School


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceRequest


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
