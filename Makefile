install:
	pipenv install --three

test:
	pipenv run python -m pytest tests/test_dato.py
