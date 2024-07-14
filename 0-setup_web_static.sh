#!/usr/bin/env bash
# Configuring Nginx for the deployment of web_static

sudo apt -qq update
sudo apt -qq -y install nginx

sudo mkdir -p /data/web_static/releases/test/

sudo mkdir -p /data/web_static/shared/

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

echo "<html>
  <head>
  </head>
  <body>
    Mohammed PBUH
  </body>
</html>" > /data/web_static/releases/test/index.html

echo "server {
	listen 80 default_server;
	listen [::]:80 default_server;


	index index.html index.htm index.nginx-debian.html;
	add_header X-Served-By"\$hostname" always;
	server_name _;

	location /hbnb_static/ {
		alias /data/web_static/current/;
		try_files "\$uri" "\$uri"/ =404;
	}

}" | sudo tee /etc/nginx/sites-available/default > /dev/null

sudo nginx -s reload

