clean: clean-coverage

coverage:
	coverage run -m pytest

clean-coverage:
	rm -rf htmlcov
	rm .coverage

test: pytest-short

pytest-short:
	@echo Running pytest
	python -m pytest --cov=omega_omnibus --tb=line

pytest-verbose:
	@echo Running pytest
	python -m pytest --cov=omega_omnibus -v

clean-pytest:
	rm -rf .pytest_cache

lint: isort black flake8 mypy pylint

isort:
	@echo Running isort
	python -m isort --diff omega_omnibus/

black:
	@echo Running black
	python -m black --check omega_omnibus/

flake8:
	@echo Running flake8
	python -m flake8 omega_omnibus/

mypy:
	@echo Running mypy
	python -m mypy omega_omnibus/

clean-mypy:
	rm -rf .mypy-cache

pylint:
	@echo Running pylint
	python -m pylint --rcfile=.pylintrc omega_omnibus/
