#!/usr/bin/env bash

apt-get install -y jq curl python3-pip openssh-server
pip3 install tornado
pip3 install pymongo
pip3 install requests

mkdir /var/janu/data/ -p
mkdir /var/janu/log/ -p
mkdir /var/janu/dockerfiles/ -p
chown janu.janu janu -R