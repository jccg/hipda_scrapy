#!/bin/sh
echo >&2 "  Connecting to WORDPRESS_DB_HOST ($WORDPRESS_DB_HOST)"
echo >&2 "  Connecting to WORDPRESS_DB_HOST ($WORDPRESS_DB_HOST)" > aaaa.txt
service nginx start && service php5-fpm start  && /usr/sbin/sshd -D 

