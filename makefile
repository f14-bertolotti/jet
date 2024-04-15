PYTHON := /usr/bin/python3

venv/bin/python3: 
	${PYTHON} -m venv venv

build: venv/bin/python3
	venv/bin/python3 -m pip install -r requirements.txt


