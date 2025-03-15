from django.urls import path
from . import views
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("challenges", views.challenges, name="challenges"),
    path("game", views.game, name="game"),
    path("ai", views.ai, name="ai")
]