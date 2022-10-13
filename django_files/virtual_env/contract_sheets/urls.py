from django.urls import path
from contract_sheets import views


urlpatterns = [
    path("ivesdale", views.ivesdale, name="ivesdale"),
]
