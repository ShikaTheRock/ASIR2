#!/bin/bash 
echo "Checking mariadb..."

if ss -lnt | grep -q ':3306 '; then
    echo "MariaDB/MySQL esta escuchando en el puerto 3306"
else
    echo "Seems that MariaDB is not installed/active"
fi
