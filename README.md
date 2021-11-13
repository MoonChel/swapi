# swapi

Service for displaying information from https://swapi.dev/

# How to run it locally

- `docker-compose up --build` - http://localhost:8000 for be, http://localhost:8080 for fe

# Possible improvements

- django vs fastapi? Can `async` improve efficiency?
- better handle for NotFound, EmptyResults and other expected exceptions
- more tests
- pre-commit hooks
- more efficient ways to work with large data? dask?
- openapi documentation?
- graphql?