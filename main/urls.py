from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.home, name="homepage"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("log-hours/", views.log_hours, name="log-hours"),
    path("view-hours/", views.view_hours, name="view-hours"),
    path("check-hours/", views.check_hours, name="check-hours"),
    path("individual-hours/<username>/", views.check_individual_hours, name="check-individual-hours"),
    path("individual-hours/<username>/", views.check_individual_hours, name="check-individual-hours"),
]