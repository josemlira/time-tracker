# time-tracker

## Run isort

isort . --check 

## Run mypy

mypy app

## Run tests

pytest

## Docker

### Create image
docker build -t time-tracker .

### Run tests or qa tools
docker run time-tracker pytest
docker run time-tracker mypy app

### Run app
docker run -it -p 8000:8000 time-tracker

or (detached)

docker run -d -p 8000:8000 time-tracker