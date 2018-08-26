from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from eduflox.api.models import Invitation, School

from .forms import InvitationForm, RegistrationForm


def home(request):
    return render(request, "agents/home.html")


@login_required
def dashboard(request):
    return render(request, "agents/dashboard.html")


@login_required
def schools(request):
    schools = School.objects.all()
    return render(request, "agents/schools.html", context=locals())


@login_required
def services(request):
    return render(request, "agents/services.html")


@login_required
def invite_agent(request):
    """Invite an agent to the portal"""
    form = InvitationForm()
    if request.method == "POST":
        form = InvitationForm(request.POST)

        if form.is_valid():
            inviter = request.user
            form.send_invitation(inviter)

            return redirect("/")

    return render(request, "invite.html", context={"form": form})


@transaction.atomic
def join(request, invitation_token):
    """Register an agent who has received an invitation"""
    invitation = get_object_or_404(Invitation, token=invitation_token)
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            invitation.accept()

            return redirect("/dashboard")

    return render(request, "join.html", context={"form": form})
