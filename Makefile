.PHONY: run

run:
	docker-compose up --build swapi_be swapi_fe

benchmark:
	docker-compose run swapi_be python benchmark.py

test:
	docker-compose run swapi_be python manage.py test swapi

clear:
	docker-compose rm