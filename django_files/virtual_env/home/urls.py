from django.urls import path
from home import views


urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login_user, name="login_user"),

]
