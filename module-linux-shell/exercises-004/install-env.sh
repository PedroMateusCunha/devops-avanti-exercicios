#!/bin/bash

sudo apt update
sudo apt install openssh-server
sudo systemctl start ssh
ssh-keyscan -H localhost >> ~/.ssh/known_hosts
ssh $USER@localhost