# Format Number

## Project Description

* The project uses flask


###  Steps to run the app

#### 1. Using Docker
```sh
$ docker-compose up
#go to http://localhost:5000/ to see the app

# To run loadtest
$ docker exec -ti flask-app locust -f tests/test_load/*.py --host http://localhost:5000

# To run unit test
$ docker exec -ti flask-app pytest tests/test_unit/*.py

# To run functional test
$ docker exec -ti flask-app pytest tests/test_functional/*.py

# To run ui test
$ docker exec -ti flask-app sh wait-for-grid.sh pytest tests/test_ui/test_home.py
```

#### 2. Without docker (in local machine)
```sh
$ export PYTHONPATH="$PYTHONPATH:/pleo_assignment/"
$ export FLASK_ENV=development #range(production|testing|development)
$ export APP_SETTINGS=development #range(development|testing|staging|production)
$ export FLASK_APP=main.py
$ flask run
# go to http://localhost:5000/ to see the app
```

2. Step to run the `unit tests`
```sh
                                           
pytest tests/test_unit/*.py
pytest tests/test_functional/*.py
```
3. Step to run the `unit tests` with `coverage report`
```sh
cd source_dir
pytest tests/test_unit/test_utils.py --cov=.
```

