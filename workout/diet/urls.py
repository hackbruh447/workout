from django.urls import path
from . import views
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("settings", views.settings, name="settings"),
    path("ai", views.ai, name="ai")
]