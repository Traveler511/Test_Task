.DEFAULT_GOAL := help
CODE = tinvest tests examples
TEST = pytest $(args) --verbosity=2 --showlocals --strict-markers --log-level=DEBUG

.PHONY: help
help:
	@echo 'Usage: make [target] ...'
	@echo ''
	@echo '    make all'
	@echo '    make install'
	@echo '    make build'
	@echo '    make clean'
	@echo '    make docs-changelog'
	@echo '    make docs-serve'
	@echo '    make docs'
	@echo '    make format'
	@echo '    make lint'
	@echo '    make mut'
	@echo '    make test-report'
	@echo '    make test-failed'
	@echo '    make test-fast'
	@echo '    make test'
	@echo ''

.PHONY: all
all: format lint test test-report build docs clean

.PHONY: update
update:
	poetry update

.PHONY: test
test:
	$(TEST) --cov

.PHONY: test-fast
test-fast:
	$(TEST) --exitfirst

.PHONY: test-failed
test-failed:
	$(TEST) --last-failed

.PHONY: test-report
test-report:
	$(TEST) --cov --cov-report html
	python -m webbrowser 'htmlcov/index.html'

.PHONY: lint
lint:
	poetry check
	flake8 --jobs 1 --statistics --show-source $(CODE)
	pylint --jobs 1 --rcfile=setup.cfg $(CODE)
	black --skip-string-normalization --line-length=88 --check $(CODE)
	pytest --dead-fixtures --dup-fixtures
	mypy $(CODE)
	# --ignore=38334 ignore pipenv for travis-ci
	# --ignore=39252 cryptography
	# --ignore=39606 cryptography
	# --ignore=39462 tornado
	# --ignore=40291 pip
	safety check --full-report --ignore=38334 --ignore=39252 --ignore=39462 --ignore=39606 --ignore=40291

.PHONY: format
format:
	autoflake --recursive --in-place --remove-all-unused-imports $(CODE)
	isort $(CODE)
	black --skip-string-normalization --line-length=88 $(CODE)
	unify --in-place --recursive $(CODE)

.PHONY: docs
docs:
	typer tinvest.cli.app utils docs --name tinvest > docs/cli.md
	mkdocs build -s -v

.PHONY: docs-serve
docs-serve:
	mkdocs serve

.PHONY: docs-changelog
docs-changelog:
	git-changelog -o CHANGELOG.md  .

.PHONY: build
build:
	poetry build

.PHONY: install
install:
	poetry install

.PHONY: clean
clean:
	rm -rf docs/cli.md || true
	rm -rf site || true
	rm -rf dist || true
	rm -rf htmlcov || true

.PHONY: mut
mut:
	mutmut run
