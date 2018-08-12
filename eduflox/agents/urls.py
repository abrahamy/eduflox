"""eduflox.agents URL Configuration"""
from django.contrib import admin
from django.urls import path
import eduflox.agents.views as views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="agents.dashboard"),
]
