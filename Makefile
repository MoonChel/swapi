.PHONY: run

run:
	docker-compose up --build

benchmark:
	docker build backend -t swapi-be -f backend/Dockerfile
	docker run swapi-be python benchmark.py