from django import forms
from django.conf import settings
from django.template.loader import render_to_string

from eduflox.api.models import Agent, Invitation, User

rendered = render_to_string("emails/invite.html", {"foo": "bar"})


class InvitationForm(forms.Form):
    email = forms.EmailField(label="Invitee Email")

    def send_invitation(self, inviter):
        """Invite new agents to the portal"""
        if not self.is_valid():
            raise Exception("Invitee email cannot be empty!")

        Invitation.create(inviter, self.cleaned_data["email"])
        # invitation = Invitation.create(request.user, self.cleaned_data["email"])
        # subject = settings.AGENT_INVITE_EMAIL_SUBJECT
        # message = settings.AGENT_INVITE_EMAIL_MESSAGE
        # user.email_user(subject, message, html_message="")


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    middle_name = forms.CharField(label="Middle Name", required=False)
    last_name = forms.CharField(label="Last Name")
    mobile_no = forms.RegexField(r"^\d{11}$")
    email = forms.EmailField(label="Email")
    address = forms.CharField(label="Address")
    city = forms.CharField(label="City")
    state = forms.CharField(label="State")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def save(self):
        """Registers a new agent"""
        if not self.is_valid():
            raise Exception("Invalid Agent Registration Form")

        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        first_name = self.cleaned_data["first_name"]
        middle_name = self.cleaned_data["middle_name"]
        last_name = self.cleaned_data["last_name"]
        mobile_no = self.cleaned_data["mobile_no"]
        address = self.cleaned_data["address"]
        city = self.cleaned_data["city"]
        state = self.cleaned_data["state"]

        user = User.objects.create_user(
            email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        agent = Agent(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            middle_name=middle_name,
            mobile_no=mobile_no,
            address=address,
            city=city,
            state=state,
        )
        agent.save()

        return agent
