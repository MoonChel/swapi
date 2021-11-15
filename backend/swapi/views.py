import csv
from datetime import datetime
from django.http import JsonResponse, HttpRequest, HttpResponseNotFound

from swapi.client.swapi.data_models import SwapiPeople
from .models import FetchFile

from .apps import swapi_client
from .csv_utils import save_csv, read_specific_lines, group_by_csv, get_new_filename

PLANETS = {}


def resolve_planets(people: SwapiPeople):
    # for better performance replace with cache, redis for example
    for person in people.results:
        if person.homeworld in PLANETS:
            person.homeworld = PLANETS[person.homeworld]
        else:
            # TODO: dirty trick, but will work
            planet_id = person.homeworld.rsplit("/")[-2]
            person.homeworld = swapi_client.get_planet_name(planet_id)
            PLANETS[person.homeworld] = person.homeworld


def fetch_swapi_to_csv_gener(request: HttpRequest):
    # load data from API via generator
    # resolve planets
    # save to csv
    # save file info to DB

    # TODO: refactor into indepedent functions
    filename = get_new_filename()

    count = 0
    with open(filename, "w") as csvfile:
        data_gen = swapi_client.get_all_people_gener()

        # TODO: not the best way, but enough for now
        data = next(data_gen)
        resolve_planets(data)
        fieldnames = data.results[0].dict().keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data.dict()["results"])

        for data in data_gen:
            resolve_planets(data)
            count += len(data.results)
            writer.writerows(data.dict()["results"])

    file = FetchFile(file=filename, count=count)
    file.save()

    return JsonResponse({"status": "ok"})


def fetch_swapi_to_csv(request: HttpRequest):
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


def get_csv_file(request: HttpRequest, file_id: int):
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


def get_csv_file_group_by(request: HttpRequest, file_id: int):
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
