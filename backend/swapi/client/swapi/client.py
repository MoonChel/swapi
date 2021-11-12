import enum
from requests import Request
from ..base import BaseClient
from .data_models import SwapiPeople


class SWAPI_ENDPOINT(enum.Enum):
    PEOPLE = "/people"
    PLANETS = "/planets"
    PLANET = "/planets/{planet_id}"


class SwapiClient(BaseClient):
    def get_people(self, page: int = 1) -> SwapiPeople:
        req = Request(
            "get",
            SWAPI_ENDPOINT.PEOPLE.value,
            params={"page": page},
        )

        # TODO: handle 404 and response with empty results
        resp = self.make_request(prep_req=req)
        people = SwapiPeople(**resp.json())

        return people

    def get_planet_name(self, planet_id: str) -> str:
        req = Request(
            "get",
            SWAPI_ENDPOINT.PLANET.value.format(planet_id=planet_id),
        )
        resp = self.make_request(req)

        return resp.json()["name"]

    def get_all_people(self):
        # TODO: better is to do it async
        # get total count from first request
        # divide by length of items in results (per_page)
        # fire count % per_page async requests and merge results into 1 object
        people = []

        page = 1

        while True:
            resp = self.get_people(page)

            people += resp.results

            if resp.next:
                page += 1
            else:
                break

        return SwapiPeople(count=len(people), results=people)
