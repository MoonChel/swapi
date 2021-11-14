import os
import timeit
from typing import Callable
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()

from swapi.views import fetch_swapi_to_csv, fetch_swapi_to_csv_gener, PLANETS


def time_fetch(func: Callable):
    num_runs = 5
    duration = timeit.Timer(lambda: func(None)).timeit(number=num_runs)

    avg_duration = duration / num_runs

    print(f"{func} - On average it took {avg_duration} seconds")


if __name__ == "__main__":
    print("benchmark for fetch and fetch generator")
    time_fetch(fetch_swapi_to_csv)
    # clear cache between run
    PLANETS.clear()
    time_fetch(fetch_swapi_to_csv_gener)
