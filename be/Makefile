
init:
	pip install -r requirements.txt
	pip install -r apps/flask/requirements.txt

run:
	$(shell env FLASK_APP=apps/flask/main.py flask run)

clean:
	$(shell find . | grep -E "(__pycache__|\.pyc|\.pyo$ )" | xargs rm -rf)

test:
	nosetests tests