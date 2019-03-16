
## Team3 Web Server Group

### Deploy script

The following script will copy the frontend and backend files to the server
at predict2019t3.biosci.gatech.edu .
It will ask for your GT username to proceed.
Please make sure you have installed `venv` and modules in `requirements.txt`
to the `backend` directory before running this script as per
`backend/README.md`.

```sh
./deploy.sh
```

### Test script

In order to test it locally, use the following script. It will launch two
servers for both frontend and backend.
Please make sure you have installed `venv` and modules in `requirements.txt`
to the `backend` directory before running this script as per
`backend/README.md`.

```sh
./serve.sh
```
