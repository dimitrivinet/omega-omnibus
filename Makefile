PACKAGE_NAME=omega_omnibus

########## GLOBAL ##########
.PHONY: clean clean-pycache lock

clean: clean-coverage clean-pytest clean-mypy clean-pycache

clean-pycache:
	find . -type d -name  "__pycache__" -exec rm -r {} +

lock:
	pip list --format=freeze > requirements-dev.txt.lock

########## SERVER ##########
.PHONY: server server-dev

server:
	uvicorn omega_omnibus:app

server-dev:
	uvicorn omega_omnibus:app --reload

########## TESTING ##########
.PHONY: coverage clean-coverage test pytest-short pytest-verbose clean-pytest

coverage:
	coverage run -m pytest

clean-coverage:
	- rm -rf htmlcov
	- rm .coverage

test: pytest-short

pytest-short:
	@echo Running pytest
	python -m pytest --cov=${PACKAGE_NAME} --tb=line

pytest-verbose:
	@echo Running pytest
	python -m pytest --cov=${PACKAGE_NAME} -v

clean-pytest:
	- rm -rf .pytest_cache

########## LINTING ##########
.PHONY: lint isort isort-dry black black-dry flake8 mypy clean-mypy pylint

lint: isort black flake8 mypy pylint

isort:
	@echo Running isort
	python -m isort ${PACKAGE_NAME}/

isort-dry:
	@echo Running isort
	python -m isort --diff ${PACKAGE_NAME}/

black:
	@echo Running black
	python -m black ${PACKAGE_NAME}/

black-dry:
	@echo Running black
	python -m black --check ${PACKAGE_NAME}/

flake8:
	@echo Running flake8
	python -m flake8 ${PACKAGE_NAME}/

mypy:
	@echo Running mypy
	python -m mypy ${PACKAGE_NAME}/

clean-mypy:
	- rm -rf .mypy_cache

pylint:
	@echo Running pylint
	python -m pylint --rcfile=.pylintrc ${PACKAGE_NAME}/
