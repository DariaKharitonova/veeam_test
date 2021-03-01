install:
	@poetry install

build: check
	@poetry build

test:
	poetry run pytest -v

lint:
	poetry run flake8 task_03 tests