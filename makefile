run-dev:
	poetry run uvicorn main:app --reload

format:
	poetry run black .
	poetry run isort .

tests:
	poetry run python -m pytest