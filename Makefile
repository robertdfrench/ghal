test: pep8 lint unit_tests
	@echo "LGTM fren"

pep8:
	tox -- flake8

lint:
	tox -- pylint ghal

unit_tests:
	tox -- pytest --cov-fail-under=100

publish_coverage:
	tox -- codecov
