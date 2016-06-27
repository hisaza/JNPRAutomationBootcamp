#!/usr/bin/env bash

sudo apt-get -y update
sudo apt-get install -y build-essential
sudo pip install -U junos-eznc==1.3.1
sudo pip install -U ansible==1.9.4
sudo ansible-galaxy remove Juniper.junos
sudo ansible-galaxy install Juniper.junos,1.3.1
