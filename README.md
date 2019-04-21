
## Team3 Web Server Group

### Requirements

The application is built with [Flask](http://flask.pocoo.org/) in python.
You may use Anaconda to install the python dependencies, the environment yml file is `final.yml`.

```
conda env create -f final.yml
```

### Test and Deployment

To test the web application on your own computer, start the flask
webserver with the following script and open your browser at
http://localhost:9981/index.html :

```sh
./serve.sh
```

Your code will be automatically (within one minute) deployed to
server (http://predict2019t3.biosci.gatech.edu/) once you push the commits to
the master branch on github.

