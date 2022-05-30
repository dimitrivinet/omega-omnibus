PACKAGE_NAME=omega_omnibus

clean: clean-coverage clean-pytest clean-mypy clean-pycache

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

lint: isort black flake8 mypy pylint

isort:
	@echo Running isort
	python -m isort --diff ${PACKAGE_NAME}/

black:
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

clean-pycache:
	find . -type d -name  "__pycache__" -exec rm -r {} +
