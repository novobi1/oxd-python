# E2E Tests

This folder contains the test scripts that are used for integration testing of 
oxd-python library. These scripts also provide examples for the use of various
functions.

## Requirements

1. OpenID Provider - Gluu Server or Google or any other OIDC respecting server
2. oxd server - oxd server should be installed locally for localhost based tests
3. Python 2.7 - for oxd-python

## Test Scripts

- `openid_socket.py` - Tests the functions relating to OpenID client like
  dynamic registration, authorization flow, logout over socket communication
  with the oxd-server.
- `openid_https.py` - Tests the functions relating to the OpenID Client over
    https with the oxd-https-extension.
 
### Running the tests

**OpenID Connect**

- Edit the host and op_host values in `openid_https.cfg` and `openid_socket.cfg`
  to suite the testing environment.
- Run `python openid_socket.py` for running the OpenID commands on oxd-server 
- Run `python openid_https.py` for running the OpenID commands on oxd-https-extension
- Run `python openid_<type>.py -v` for verbose output of each command
- Run `python openid_<type>.py -h` for help.

**UMA**

- Edit the host and op_host values in `uma_https.cfg` and `uma_socket.cfg`
  to suite the testing environment.
- Run `python uma_socket.py` for running the UMA commands on oxd-server 
- Run `python uma_https.py` for running the UMA commands on oxd-https-extension
- Run `python uma_<type>.py -v` for verbose output of each command
- Run `python uma_<type>.py -h` for help.