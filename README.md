# time-tracker

## Run isort

```bash
isort . --check 
```

## Run mypy

```bash
mypy app
```

## Run tests

```bash
pytest
```

## Docker

### Create image

```bash
docker build -t time-tracker .
```

### Run tests or qa tools

```bash
docker run time-tracker pytest
docker run time-tracker mypy app
```

### Run app

```bash
docker run -it -p 8000:8000 time-tracker
```

or (detached)

```bash
docker run -d -p 8000:8000 time-tracker
```