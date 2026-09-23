#!/bin/bash 
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
