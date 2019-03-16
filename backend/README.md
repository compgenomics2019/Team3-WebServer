Computational Genomics Team 3
Backend Server

Using [Flask](http://flask.pocoo.org/)

## Software versions
```
pip 19.0.3
Python 3.7.1
```

## Server Installation
```
git clone git@github.gatech.edu:compgenomics2019/Team3-WebServer.git
cd Team3-WebServer/predictive_webserver_team3_backend
```

create virtualenv and activate it

```
python3 -m venv venv
. venv/bin/activate
```

Install software with correct versions, and run Flask server
```
pip3 install -r requirements.txt --no-index
export FLASK_APP=server.py  FLASK_ENV=development
flask run

```
Open http://127.0.0.1:5000/
