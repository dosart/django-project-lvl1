install:
	@poetry install

run_server:
	poetry run python3 manage.py runserver

create_project:
	poetry run python3 manage.py startapp $(name)

format:
	poetry run black generator/

lint:
	poetry run flake8 generator/views.py

selfcheck:
	poetry check

check:
	@make selfcheck
	@make format
	@make lint

.PHONY: install run_server create_project format lint selfcheck check