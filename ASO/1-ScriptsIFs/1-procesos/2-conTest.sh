#!/bin/bash 

#Variables 

## Si online es 0 no hay conectividad 
online=0 

#Comprobacion conectividad 
#nslookup -q tic.ieslasenia.org >/dev/null 
nslookup -q shikatherock.neocities.org >/dev/null 

if [ $? -eq 0 ]; then 
    echo "User is online..."
    sleep 1
else
    echo "No internet conection [ERROR_1]"
    exit 1
fi 
