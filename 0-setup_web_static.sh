#!/usr/bin/env bash
# Install nginx and configure web static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "Hello, this is a test HTML file." | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/server {/a \
    location /hbnb_static {\
        alias /data/web_static/current/;\
    }\
' /etc/nginx/sites-available/default

sudo service nginx restart
