# UDA Python coding test
## Overview :male_detective:
The goal is to deploy an HTTP REST API service that allows to create assets into a database.

The following libraries and frameworks were used:
- [Django](https://pypi.org/project/Django/)
- [django-heroku](https://pypi.org/project/django-heroku/)
- [djangorestframework](https://pypi.org/project/djangorestframework/)
- [drf-yasg](https://pypi.org/project/drf-yasg2/)
- [gunicorn](https://pypi.org/project/gunicorn/)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)

## Environment variables 📋

Some variables are expected to exist into the environment. In my development environment I'm using and `.env` file 
with these properties:
```properties
DEBUG=True
SECRET_KEY=
PORT=8000
DATABASE_HOST=db
DATABASE_PORT=5432
POSTGRES_DB=test
POSTGRES_USER=test
POSTGRES_PASSWORD=test
```


## Running the application 🚀
```bash
docker-compose up
```
Endpoints should be accessible on port `8000` of `localhost`.

## Endpoints documentation 📖

Endpoints full documentation can be found at:
```http request
http://localhost:8000/swagger/
```
```http request
https://uda-coding-test.herokuapp.com/swagger/
```

![Alt text](images/swagger.png?raw=true "Swagger documentation")

## Running the tests 🛠

```bash
docker-compose run web python manage.py test
```

### Continuous Integration :white_check_mark:

|master|development|
| ------------- | ------------- |
[![CircleCI](https://circleci.com/gh/Garcel/uda-coding-test/tree/master.svg?style=shield)](https://circleci.com/gh/Garcel/uda-coding-test/tree/master.svg?style=shield)|[![CircleCI](https://circleci.com/gh/Garcel/uda-coding-test/tree/development.svg?style=shield)](https://circleci.com/gh/Garcel/uda-coding-test/tree/development.svg?style=shield)

## Check it out at Heroku :beers:

```http request
https://uda-coding-test.herokuapp.com/assets/
```

## Author :writing_hand:
José Antonio Garcel (garcel.developer@gmail.com)

Nov 29 2020