from django.urls import path

from .views import fetch_swapi_people, get_csv, get_csv_group_by

urlpatterns = [
    path("fetch/", fetch_swapi_people, name="fetch"),
    path("fetch-csv/<int:file_id>", get_csv, name="get-csv"),
    path("group-by-csv/<int:file_id>", get_csv_group_by, name="group-by-csv"),
]
