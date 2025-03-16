from django.urls import path
from . import views
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("settings", views.settings, name="settings"),
    path("ai", views.ai, name="ai"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("get_user_data", views.get_user_data, name="leaderboard")
]