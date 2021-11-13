import csv
import petl as etl
from datetime import datetime
from typing import List, Dict, Tuple


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

        return header, list(table[1:10])

    results = list(etl.valuecounts(table, *fields))
    header = results.pop(0)

    return header, results
