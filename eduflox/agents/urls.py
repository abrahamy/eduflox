"""eduflox.agents URL Configuration"""
from django.urls import path
import eduflox.agents.views as views

urlpatterns = [path("", views.dashboard, name="agents.dashboard")]
