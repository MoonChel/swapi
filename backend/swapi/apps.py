from django.apps import AppConfig

from swapi.client.swapi import SwapiClient
from swapi.client import BaseClientConfig


swapi_client = SwapiClient(BaseClientConfig("https://swapi.dev/api"))


class SwapiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "swapi"
