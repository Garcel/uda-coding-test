# UDA Python coding test
Deploy an HTTP REST API service that allows to create assets into a database.

### Environment variables

Some variables are expected to exist into the environment. In my development environment I'm using and `.env` file 
with these properties:
```properties
DEBUG=on
SECRET_KEY=
PORT=8000
DATABASE_HOST=db
DATABASE_PORT=5432
POSTGRES_DB=test
POSTGRES_USER=test
POSTGRES_PASSWORD=test
```


## Usage

Run:
```bash
docker-compose up --build
```
Endpoints should be accessible on port `8000` of `localhost`.

## Endpoints

Endpoints full documentation can be found at:
```http request
http://localhost:8000/swagger/
```

![Alt text](images/swagger.png?raw=true "Swagger documentation")

## Running the tests

```bash
docker-compose run web python manage.py test
```

### Continuous Integration

|master|development|
| ------------- | ------------- |
[![CircleCI](https://circleci.com/gh/Garcel/uda-coding-test/tree/master.svg?style=shield)](https://circleci.com/gh/Garcel/uda-coding-test/tree/master.svg?style=shield)|[![CircleCI](https://circleci.com/gh/Garcel/uda-coding-test/tree/development.svg?style=shield)](https://circleci.com/gh/Garcel/uda-coding-test/tree/development.svg?style=shield)