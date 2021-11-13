from django.urls import path

from .views import (
    fetch_swapi_to_csv,
    fetch_swapi_to_csv_gener,
    get_csv_file,
    get_csv_file_group_by,
    get_fetch_files,
)

urlpatterns = [
    path("fetch/", fetch_swapi_to_csv, name="fetch"),
    path("fetch-gener/", fetch_swapi_to_csv_gener, name="fetch-gener"),
    path("files/", get_fetch_files, name="get-fetch-files"),
    path("fetch-csv/<int:file_id>", get_csv_file, name="get-csv"),
    path("group-by-csv/<int:file_id>", get_csv_file_group_by, name="group-by-csv"),
]
