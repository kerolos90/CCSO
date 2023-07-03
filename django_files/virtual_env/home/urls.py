from django.urls import path
from home import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name="home"),
    path("change_password/", auth_views.PasswordChangeView.as_view(), name="change_password"),
    path("forms", views.forms, name="forms"),
    path("ehd", views.ehd, name="ehd"),
    path("employee_assignments", views.employee_assignments, name="employee_assignments"),
]
