install:
	pipenv install --three
	pip3 install numpy

test:
	pipenv run python -m pytest tests/test_estacion.py
