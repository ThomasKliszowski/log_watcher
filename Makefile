ENV=venv/bin
ifdef VIRTUAL_ENV
	ENV=$(VIRTUAL_ENV)/bin
endif

upload:
	$(ENV)/python setup.py sdist register upload
	rm -rf dist
