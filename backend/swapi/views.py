import csv
from typing import List, Dict, Tuple
from django.http import JsonResponse, HttpRequest, HttpResponseNotFound
from datetime import datetime
import petl as etl

from swapi.client.swapi.data_models import SwapiPeople
from .models import FetchFile

from .apps import swapi_client


def save_csv(data: List[Dict]) -> str:
    now = datetime.now()
    filename = f"{now}.csv"

    with open(filename, "w") as csvfile:
        fieldnames = data[0].keys()

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    return filename


def read_specific_lines(
    filename: str, start: int, end: int
) -> Tuple[List[str], List[List]]:
    table = etl.fromcsv(filename)

    header = etl.header(table)

    # +1 because of header
    return header, list(table[start + 1 : end + 1])


def group_by_csv(filename: str, fields: List[str]) -> Tuple[List[List], List[List]]:
    table = etl.fromcsv(filename)

    if not fields:
        header = etl.header(table)

        return header, list(table[1:])

    results = list(etl.valuecounts(table, *fields))
    header = results.pop(0)

    return header, results


def resolve_planets(people: SwapiPeople):
    # for better performance replace with cache, redis for example
    planets = {}

    for person in people.results:
        if person.homeworld in planets:
            person.homeworld = planets[person.homeworld]
        else:
            # TODO: dirty trick, but will work
            planet_id = person.homeworld.rsplit("/")[-2]
            person.homeworld = swapi_client.get_planet_name(planet_id)
            planets[person.homeworld] = person.homeworld


def fetch_swapi_people(request: HttpRequest):
    # load data from API
    # resolve planets
    # save to csv
    # save file info to DB

    people = swapi_client.get_all_people()
    resolve_planets(people)

    filename = save_csv(people.dict()["results"])

    file = FetchFile(file=filename, count=people.count)
    file.save()

    return JsonResponse({"status": "ok"})


def get_fetch_files(request: HttpRequest):
    files = FetchFile.objects.all()

    return JsonResponse(
        {
            "items": [
                {
                    "id": f.id,
                    "created_at": f.created_at,
                }
                for f in files
            ],
        }
    )


def get_csv(request: HttpRequest, file_id: int):
    # load file
    # load data from csv
    page = int(request.GET.get("page", 1))

    # can be also get request param
    per_page = 10

    file = FetchFile.objects.get(id=file_id)
    if not file:
        raise HttpResponseNotFound("File not found")

    start = page * per_page
    end = start + per_page
    header, results = read_specific_lines(file.file, start, end)

    return JsonResponse(
        {
            "header": header,
            "results": results,
            "created_at": file.created_at,
        }
    )


def get_csv_group_by(request: HttpRequest, file_id: int):
    fields = request.GET.get("fields", [])
    if fields:
        fields = fields.split(",")

    file = FetchFile.objects.get(id=file_id)
    if not file:
        raise HttpResponseNotFound("File not found")

    header, results = group_by_csv(file.file, fields)

    return JsonResponse(
        {
            "results": results,
            "header": header,
            "created_at": file.created_at,
        }
    )
