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


class UserStringRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        obj = models.User.objects.get(username=value)
        return f"{obj.first_name} {obj.last_name}"


class ServiceSerializer(serializers.ModelSerializer):
    school_name = serializers.StringRelatedField(many=False, source="school.name")
    agent = UserStringRelatedField(many=False, source="requested_by")

    class Meta:
        model = models.Service
        fields = "__all__"
        extra_kwargs = {"requested_by": {"default": serializers.CurrentUserDefault()}}


class SchoolSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = models.School
        fields = "__all__"
        extra_kwargs = {"created_by": {"default": serializers.CurrentUserDefault()}}


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    agent = AgentSerializer(read_only=True)
    invitations = InvitationSerializer(read_only=True)
    schools = SchoolSerializer(many=True, read_only=True)
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = models.User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "agent",
            "invitations",
            "schools",
            "services",
        )
