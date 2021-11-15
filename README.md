# swapi

Service for displaying information from https://swapi.dev/

# How to run it locally

- `make run` - http://localhost:8000 for be, http://localhost:8080 for fe, and csv files saved in mounted volume `backend/csv_files`
- `make benchmark` - to benchmark fetch and fetch implemented via generator
- `make test` - run tests
# Possible improvements

- improve naming
- django vs fastapi? Can `async` improve efficiency?
- better handle for NotFound, EmptyResults and other expected exceptions
- more tests
- pre-commit hooks
- more efficient ways to work with large data? dask?
- openapi documentation?
- add logging, metrics, monitors


# Benchmark

- <function fetch_swapi_to_csv at 0xffffabc3adc0> - On average it took 5.315709011000581 seconds
- <function fetch_swapi_to_csv_gener at 0xffffabc3ad30> - On average it took 5.049909185597789 seconds