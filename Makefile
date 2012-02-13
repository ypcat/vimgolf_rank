.PHONY: templates clean update update-local

templates/__init__.py: templates/*.html
	python web/template.py --compile templates

templates: templates/__init__.py

clean:
	find . -name '*.pyc' -delete

update:
	curl -d '' http://vimgolf-rank.appspot.com/

update-local:
	curl -d '' http://localhost:8080

