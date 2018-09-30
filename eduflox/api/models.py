import random
import uuid

from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from rest_framework.authtoken.models import Token

User = get_user_model()


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Agent(models.Model):
    MOBILE_NUMBER_VALIDATOR = RegexValidator(
        regex=r"^\d{11}$", message="Invalid mobile number."
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="agent")
    first_name = models.CharField("First Name", max_length=25)
    middle_name = models.CharField("Middle Name", max_length=25, null=True)
    last_name = models.CharField("Last Name", max_length=25)
    mobile_no = models.CharField(
        "Mobile No", max_length=11, validators=[MOBILE_NUMBER_VALIDATOR]
    )
    email = models.EmailField("Email")
    address = models.CharField("Street", max_length=200)
    city = models.CharField("City", max_length=25)
    state = models.CharField("State", max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "first_name", "last_name"]


def create_token():
    """Create a random token string"""
    return str(uuid.uuid4()).replace("-", "")


class Invitation(models.Model):
    inviter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="invitations"
    )
    invitee_email = models.EmailField("Invitee Email")
    token = models.CharField("Token", max_length=75, unique=True, default=create_token)
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

    class Meta:
        ordering = ["-invitation_date", "inviter"]


class School(models.Model):
    STATUSES = (
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    )
    name = models.CharField("School", max_length=150)
    location = models.CharField("Location", max_length=25)
    district = models.CharField("District", max_length=25)
    code = models.CharField(
        "School Code", max_length=10, unique=True, null=True, blank=True
    )
    status = models.CharField(
        "Status", max_length=20, choices=STATUSES, default="pending"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="schools"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _derive_school_code(self):
        """Generate a school code when inserting a new record"""
        if self.code:
            return self.code

        # target format = '{district:04d}{location:02d}{school:04d}'
        # @todo: reimplement with the correct codes rather than random numbers
        district = random.randrange(0, 9999)
        location = random.randrange(0, 99)
        school = random.randrange(0, 9999)

        code = "{district:04d}{location:02d}{school:04d}".format(
            district=district, location=location, school=school
        )
        return code

    def save(self, **kwargs):
        self.code = self._derive_school_code()
        return super(School, self).save(**kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at", "name"]


class Service(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="services"
    )
    service_description = models.TextField()
    requested_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="services"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "school"]


class Invoice(models.Model):
    request_code = models.ForeignKey(Service, on_delete=models.CASCADE)
    cpe = models.CharField("Add CPE", max_length=75)
    cpe_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
