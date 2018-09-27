import rest_framework.serializers as serializers
import eduflox.api.models as models


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agent
        fields = "__all__"
        extra_kwargs = {"user": {"read_only": True}}


class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invitation
        fields = "__all__"


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.School
        fields = "__all__"
        extra_kwargs = {"created_by": {"default": serializers.CurrentUserDefault()}}


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = "__all__"
        extra_kwargs = {"requested_by": {"default": serializers.CurrentUserDefault()}}


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = "__all__"
