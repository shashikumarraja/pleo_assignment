# Format Number

## Project Description

* The project uses flask


###  Step to run the app

In the top-level directory:
```sh
$ export PYTHONPATH="$PYTHONPATH:/top_level_dir/"
$ export FLASK_ENV=development #range(production|testing|development)
$ export APP_SETTINGS=development #range(development|testing|staging|production)
$ export FLASK_APP=main.py
$ flask run
```

2. Step to run the `unit tests`
```sh
export PYTHONPATH="$PYTHONPATH:/top_level_dir/"                                             
pytest tests/test_unit/*.py
pytest tests/test_functional/*.py
```
3. Step to run the `unit tests` with `coverage report`
```sh
cd source_dir
pytest tests/test_unit/test_utils.py --cov=.
```

