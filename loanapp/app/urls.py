from .views import login, home, signup, logout
from django.urls import path, re_path

app_name = 'app'

urlpatterns = [
    path("home/", home, name='home'),
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path("logout/", logout, name="logout")
]

