from django.urls import path

from .views import fetch_swapi_people, get_csv, get_csv_group_by, get_fetch_files

urlpatterns = [
    path("fetch/", fetch_swapi_people, name="fetch"),
    path("files/", get_fetch_files, name="get-fetch-files"),
    path("fetch-csv/<int:file_id>", get_csv, name="get-csv"),
    path("group-by-csv/<int:file_id>", get_csv_group_by, name="group-by-csv"),
]
