.PHONY: templates clean

templates/__init__.py: templates/*.html
	python web/template.py --compile templates

templates: templates/__init__.py

clean:
	find . -name '*.pyc' -delete

