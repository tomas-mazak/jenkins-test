test:
	python3 -m pytest --cov=useless --cov-report xml:cobertura.xml --cov-report term-missing
