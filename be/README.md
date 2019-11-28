Back-end part 
=======
 Provide back-end example following [clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) design concepts. 

 * ```breadpan``` package : Base classes
 * ```todo``` package : To-Do business logic by using breadpan package. 
 * ```apps ``` : RESTful API server example by using todo package.

 Concepts
 -----
 * ```todo``` package 

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

Init 
-----
```shell
make init
```

Run
-----
```shell
make run
```

Test
-----
```shell
make test
```

Clean up
-----
```shell
make clean
```