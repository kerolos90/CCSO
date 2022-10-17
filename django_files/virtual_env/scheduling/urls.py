from django.urls import path
from scheduling import views


urlpatterns = [
    path("patrol_schedule", views.patrol_schedule, name="patrol_schedule"),
    path("investigation_schedule", views.investigation_schedule),
]
