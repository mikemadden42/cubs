setup:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip3 install -r requirements.txt; \

run:
	. venv/bin/activate; \
	python3 speedtest.py \

freeze:
	. venv/bin/activate; \
	pip3 install Pillow matplotlib pandas requests urllib3 --upgrade; \
	pip3 freeze > requirements.txt; \

.PHONY: freeze run setup
