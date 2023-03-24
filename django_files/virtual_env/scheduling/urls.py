from django.urls import path
from scheduling import views


urlpatterns = [
    path("patrol_schedule", views.patrol_schedule, name="patrol_schedule"),
    path("edit_schedule", views.edit_schedule, name="edit_schedule"),
    path("patrol_schedule_partial/", views.patrol_schedule_partial, name="patrol_schedule_partial"),
    path("delete_other_row/", views.delete_other_row, name="delete_other_row"),
    path("add_other_row/", views.add_other_row, name="add_other_row"),
    path("time_off_request/", views.time_off_request, name="time_off_request"),

]
