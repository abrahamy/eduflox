"""eduflox.agents URL Configuration"""
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

import eduflox.api.views as views


router = DefaultRouter()
router.register(r"agents", views.AgentViewSet, base_name="agent")
router.register(r"invitations", views.InvitationViewSet, base_name="invitation")
router.register(r"schools", views.SchoolViewSet, base_name="school")
router.register(r"services", views.ServiceViewSet, base_name="service")
router.register(r"invoices", views.InvoiceViewSet, base_name="invoice")

urlpatterns = [path("auth", obtain_auth_token, name="api.token")]
urlpatterns.extend(router.urls)
