from django.urls import path
from field_training import views


urlpatterns = [
    path("", views.field_training, name="field_training"),
]
