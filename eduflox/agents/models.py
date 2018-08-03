import uuid

from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

User = get_user_model()


class Agent(models.Model):
    MOBILE_NUMBER_VALIDATOR = RegexValidator(
        regex=r"^\d{11}$", message="Invalid mobile number."
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField("First Name")
    middle_name = models.CharField("Middle Name", null=True)
    last_name = models.CharField("Last Name")
    mobile_no = models.CharField("Mobile No", validators=[MOBILE_NUMBER_VALIDATOR])
    email = models.EmailField("Email")
    address = models.CharField("Street")
    city = models.CharField("City")
    state = models.CharField("State")


def create_token():
    """Create a random token string"""
    return str(uuid.uuid4()).replace("-", "")


class Invitation(models.Model):
    inviter = models.ForeignKey(User, on_delete=models.SET_NULL)
    invitee_email = models.EmailField("Invitee Email", unique=True)
    token = models.CharField("Token", unique=True, default=create_token)
    invitation_date = models.DateTimeField(auto_now_add=True)
    accepted_date = models.DateTimeField(null=True)

    def accept(self):
        """Accept the invitation"""
        self.accepted_date = timezone.now()
        self.save()

    @classmethod
    def create(cls, inviter, invitee_email):
        """Creates a new invitation"""
        invitation = cls(inviter=inviter, invitee_email=invitee_email)
        invitation.save()

        return invitation


class School(models.Model):
    name = models.CharField("School")
    location = models.CharField("Location")
    district = models.CharField("District")
    code = models.CharField("School Code", unique=True)


class ServiceRequest(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    service_description = models.TextField()


class Invoice(models.Model):
    request_code = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    cpe = models.CharField("Add CPE", max_length=75)
    cpe_amount = models.DecimalField()
