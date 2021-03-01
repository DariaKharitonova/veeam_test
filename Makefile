install:
	@poetry install

lint:
	poetry run flake8 task_03 tests

test:
	poetry run pytest -v

coverage:
	poetry run pytest --cov=task_03 --cov-report xml