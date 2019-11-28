Back-end part 
=======
Simple RESTful API 

Requirements
------
* python3
* flask
* flask_restful 

Setup
-------
```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install -r apps/flask/requirements.txt 
```

Run
-----
```shell
env FLASK_APP=apps/flask/main.py flask run
```

Clean up
-----
```shell
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```