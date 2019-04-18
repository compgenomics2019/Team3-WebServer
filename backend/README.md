Computational Genomics Team 3
Backend Server

Using [Flask](http://flask.pocoo.org/)

## Software versions
```
pip 19.0.3
Python 3.7.1
```

## Set up venv and install dependencies

For a fresh clone of the repository, you need following steps
to install the dependencies for backend server.

**Within `backend` directory**, run the following command:

```
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
deactivate
```

Then go back to the parent directory and run:

```
./serve.sh
```

Checkout http://127.0.0.1:5000/

## Email

`mail.py` is a script for sending user an email notification.
It can be either used as a standalone script or as a python module:

```sh
./mail.py --to jialin@gatech.edu --resid test1
```

In python:

```python3
import mail
mail.send("jialin@gatech.edu", "test1")
```


