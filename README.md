# ssl-validator

#### Instructions

##### Local Testing
1) Start local https web server
    - A test server.py script & cert .pem file have been included
    - If using the server.py script, pass ```localhost 4444``` as command line arguments
```sh
python3 server.py   # if using included test server
python3 cert_validity_local.py localhost 4444   # use your local hostname/ip
```

##### Remote Testing
1) Pass web address as an argument
```sh
python3 cert_validity_remote.py sap.com   # use any domain name
```