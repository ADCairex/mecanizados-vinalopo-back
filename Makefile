.PHONY: lint format test

run:
	uvicorn main:app --reload

lint:
	flake8 --jobs=1 ./

format:
	black ./ --config format.toml
	isort ./ --settings-path format.toml

test:
	coverage run --rcfile=coverage -m pytest
	coverage html -o coverage/coverage-report.html