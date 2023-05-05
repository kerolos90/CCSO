from django.urls import path
from contract_sheets import views


urlpatterns = [
    path("ivesdale", views.ivesdale, name="ivesdale"),
    path("philo", views.philo, name="philo"),
    path("savoy", views.savoy, name="savoy"),
    path("st_joseph", views.st_joseph, name="st_joseph"),
    path("add_contract_sheet", views.add_contract_sheet, name="add_contract_sheet"),
    path("save_contract_sheet", views.save_contract_sheet, name="save_contract_sheet"),
    path("monthly_totals", views.monthly_totals, name="monthly_totals"),
    path("contract_sheets_card", views.contract_sheets_card, name="contract_sheets_card"),
    path("view_contract_sheet/<int:id>/<str:village>/", views.view_contract_sheet, name="view_contract_sheet"),
    path("delete_contract_sheet/<int:id>", views.delete_contract_sheet, name="delete_contract_sheet"),
]

