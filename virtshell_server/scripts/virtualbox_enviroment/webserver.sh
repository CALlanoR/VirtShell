#!/usr/bin/env bash

sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile

# perl -e 'printf("%s\n", crypt("janu", "password"))'
useradd -m -p paSW9tsGADOSY -s /bin/bash janu
echo 'janu	ALL=(ALL:ALL) ALL' >> /etc/sudoers

mkdir /var/janu -p
mkdir /var/janu/files/ -p
mkdir /var/janu/files/ -p
chown janu.janu /var/janu -R

apt-get install -y jq curl python3-pip openssh-server
pip3 install tornado
pip3 install pymongo
pip3 install requests

