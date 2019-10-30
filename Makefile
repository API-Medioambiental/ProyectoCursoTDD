install:
	pipenv install --three

test:
	pipenv run python -m pytest test_dato.py
