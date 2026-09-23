#!/bin/bash 

#Vbox test 
groups | grep -q "vboxusers" 

if [ $? -eq 0 ]; then 
    sleep 1
    echo "Vboxuser is found, continuing..."
else
    sleep 1
    echo "Vboxuser is NOT found, please solve that issue"

fi