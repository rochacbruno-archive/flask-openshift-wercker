# flask-openshift-wercker
Flask APP to run on OpenShift with automatic deploys by WerckerCI

[![wercker status](https://app.wercker.com/status/c5be8a1368d54576b58dce3381504d63/m "wercker status")](https://app.wercker.com/project/bykey/c5be8a1368d54576b58dce3381504d63)

# A simple calculator API

```
pip install -r requirements.txt
python app.py
```

then

- http://localhost:5000/calc/sum/1/2
> {"result": 3}

Operations are: **sum**, **sub**, **mul**, **div**

# Swagger API

The Swagger API is available at:

http://localhost:5000/apidocs/index.html


## Fork this REPO

Create a fork on your own github account

##  Set a new application on OpenShift using this template:

> click the link below and change the git url to your own repo

[![Launch on OpenShift](http://launch-shifter.rhcloud.com/button.svg)](https://openshift.redhat.com/app/console/application_type/custom?cartridges%5B%5D=python-2.7&initial_git_url=https://github.com/rochacbruno/flask-openshift-wercker.git&name=calculator&initial_git_branch=master)

## Create a new deployment step on WerckerCI

- Create your wercker account
- Register a new application: https://app.wercker.com/#applications/create using your forked repo
- Trigger a build and see it passing

## Setup a deployment to OpenShift

- Create an access token on OPenShift https://openshift.redhat.com/app/console/authorizations/new
- Paste this access token on wercker deploy page https://app.wercker.com/#applications/YOUR_APP_ID/settings/targets/openshift
- Then Wwercker will create an SSH Key for you, add this key to your OPenShift panel https://openshift.redhat.com/app/console/keys/new
- select [x] Auto Deploy on successful build
- DONE! in the next github commit the deployment will be automatic
