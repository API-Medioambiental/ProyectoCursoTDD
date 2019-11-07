install:
	pipenv install --three
	pipenv run pip install pytest-cov

test:
	pipenv run python -m pytest tests/test_estacion.py
	pipenv run python -m pytest --cov=estacion tests/

