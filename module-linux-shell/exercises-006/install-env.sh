#!/bin/bash

echo "#ignore comment lines
#users
[user]
name=cicerow
role=admin
[user]
name=sss
role=read-only
#functions
[functions]
net=on
firewall=off
debug=on" > /tmp/file-test.cfg