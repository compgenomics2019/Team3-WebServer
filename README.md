
## Team3 Web Server Group

### Test and Deployment

Please follow `backend/README.md` to install `venv` and modules
in `requirements.txt to the `backend` directory.

To test the web application on your own computer, start the flask
webserver with the following script and open your browser at
http://localhost:9981/index.html :

```sh
./serve.sh
```

Your code will be automatically (within one minute) deployed to the
server once you push to the master branch on github.
However, currently there are some configuration issues with the
proxy of the server. To use the application on server, please
run `./server_proxy.sh` and open your browser at
http://localhost:8864/index.html . The script will setup a
proxy between your computer and the server port at 9981.


