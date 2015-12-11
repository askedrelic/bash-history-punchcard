install: env/bin/python

env/bin/python:
	virtualenv env

pip:
	env/bin/pip install -r requirements.txt

clean:
	rm -rf env/
