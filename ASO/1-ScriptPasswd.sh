#!/bin/bash 

#Variables 

## Si online es 0 no hay conectividad 
online=0 

##Prof 0 - fail, prof 1 - profesor, prof 2 - alumno 
prof=0

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


# Profesor / alumno test 
groups | grep -q "ALU_FP_A3" 


if [ $? -eq 0 ]; then 
    echo "You are a Alumno User" 
fi 

groups | grep -q "Docente_A3" 

if [ $? -eq 0 ]; then 
    echo "You are a Docente User"
else
    echo "You are a Default User"
fi
#Vbox test 
groups | grep -q "vboxusers" 

if [ $? -eq 0 ]; then 
    sleep 1
    echo "Vboxuser is found, continuing..."
else
    sleep 1
    echo "Vboxuser is NOT found, please solve that issue"

fi

echo "Guessing hashes..."
sleep 3
echo "Hashes found!"
# Shell test 
for op in $(cat /etc/passwd | grep -v nologin$ | grep -v false$ | grep -v sync$ | awk -F ":" '{print $1}'); do 

    alg=$(cat /etc/shadow | grep $op | awk -F ":" '{print $2}' |  awk -F "$" '{print $2}')
    if [ ! -z $alg ]; then

        case "$alg" in
            1)
                crypt="MD5"
                ;;
            2a|2b|2x|2y)
                crypt="Blowfish / bcrypt"
                ;;
            5)
                crypt="SHA-256"
                ;;
            6)
                crypt="SHA-512"
                ;;
            y)
                crypt="yescrypt"
                ;;
            7)
                crypt="scrypt"
                ;;
            *)
                crypt="Desconocido"
                ;;
        esac

        echo "$op -> $crypt"

    else
        echo $op has no password
    fi
done 

#Reescribir config default de vim

echo "Setting user vim config as default..."
sleep 1
#cp ~/.vimrc /etc/vim/vimrc

echo "Checking mariadb..."

if ss -lnt | grep -q ':3306 '; then
    echo "MariaDB/MySQL esta escuchando en el puerto 3306"
else
    echo "Seems that MariaDB is not installed/active"
fi
