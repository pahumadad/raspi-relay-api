Raspberry Pi Temperature Control
================================

Instalation
-----------

You have to install python3 venv to create the virtual environment.

```
$ sudo apt-get install python3-venv
$ python3 -m venv env
```

Then, you have to install all packages needed:

`$ env/bin/pip install -r requirements.txt`


Run
---

You have to set the Flask app as environment variable.
`$ export FLASK_APP=$(pwd)/relay_api/__main__.py`

Next you can run the relay server api with:
`python -m flask run --host=0.0.0.0 --debugger`
