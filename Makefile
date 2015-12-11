install: env/bin/python

env/bin/python:
	virtualenv env

pip:
	env/bin/pip install -r requirements.txt

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
