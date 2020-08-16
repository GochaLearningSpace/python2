#! /bin/bash -f

# install my sql
echo "install my sql"
sudo apt-get update
sudo apt-get install mysql-server

sudo mysql_secure_installation utility

# allow remote access 
echo "allow remote access"
sudo systemctl enable mysql
