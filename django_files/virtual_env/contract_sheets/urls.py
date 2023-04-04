from django.urls import path
from contract_sheets import views


urlpatterns = [
    path("ivesdale", views.ivesdale, name="ivesdale"),
    path("add_contract_sheet", views.add_contract_sheet, name="add_contract_sheet"),

]
