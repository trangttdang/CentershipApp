from django.urls import path
from . import views


app_name = "profiles"   


urlpatterns = [
    # path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("mentor_signup", views.mentor_request, name="mentor_register"),
    path("mentee_signup", views.mentee_request, name="mentee_register"),
    path("mentor_profile", views.mentor_profile_request, name="mentor_profile"),
    path("mentee_profile", views.mentee_profile_request, name="mentee_profile"),
]