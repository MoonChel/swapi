import pytest
from typing import List

from django.urls import reverse
from django.test import TestCase

from swapi.models import FetchFile
from swapi.apps import swapi_client
from swapi.client.swapi.data_models import SwapiPeople


class SwapiClientTest(TestCase):
    @pytest.mark.vcr()
    def test_swapi_client(self):
        people: SwapiPeople = swapi_client.get_people()

        self.assertIsNotNone(people.count)
        self.assertIsNotNone(people.next)
        self.assertIsInstance(people.results, List)


class ViewsTest(TestCase):
    def setUp(self) -> None:
        self.file = FetchFile(file="test_file.csv", count=100)
        self.file.save()

    @pytest.mark.vcr()
    def test_fetch(self):
        resp = self.client.get(reverse("fetch"))

        self.assertEqual(resp.status_code, 200)

    @pytest.mark.vcr()
    def test_fetch_gener(self):
        resp = self.client.get(reverse("fetch-gener"))

        self.assertEqual(resp.status_code, 200)

    @pytest.mark.vcr()
    def test_get_csv_file(self):
        resp = self.client.get(
            reverse(
                "get-csv",
                kwargs={"file_id": self.file.id},
            ),
        )

        self.assertEqual(resp.status_code, 200)

    @pytest.mark.vcr()
    def test_group_by_csv(self):
        resp = self.client.get(
            reverse(
                "group-by-csv",
                kwargs={"file_id": self.file.id},
            ),
            {"fields": "homeworld,birth_year"},
        )

        self.assertEqual(resp.status_code, 200)

    @pytest.mark.vcr()
    def test_get_fetch_files(self):
        resp = self.client.get(reverse("get-fetch-files"))

        self.assertEqual(resp.status_code, 200)
