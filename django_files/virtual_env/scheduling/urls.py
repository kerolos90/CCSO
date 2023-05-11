from django.urls import path
from scheduling import views


urlpatterns = [
    path("patrol_schedule", views.patrol_schedule, name="patrol_schedule"),
    path("edit_schedule", views.edit_schedule, name="edit_schedule"),
    path("patrol_schedule_partial/", views.patrol_schedule_partial, name="patrol_schedule_partial"),
    path("delete_other_row/<int:id>", views.delete_other_row, name="delete_other_row"),
    path("add_other_row/", views.add_other_row, name="add_other_row"),
    path("time_off_request/", views.time_off_request, name="time_off_request"),
    path("benefit_time_table/", views.benefit_time_table, name="benefit_time_table"),
    path("benefit_time_review/", views.benefit_time_review, name="benefit_time_review"),
    path("benefit_time_review/<int:id>", views.benefit_time_review, name="benefit_time_review"),
    path("benefit_requests/", views.benefit_requests, name="benefit_requests"),
    path("my_benefit_requests/", views.my_benefit_requests, name="my_benefit_requests"),
    path("my_benefit_time_table/", views.my_benefit_time_table, name="my_benefit_time_table"),
    path("delete_my_request/<int:id>", views.delete_my_request, name="delete_my_request"),

]
