#!/bin/bash -x

##Prof 0 - fail, prof 1 - profesor, prof 2 - alumno 
prof=0

# Profesor / alumno test 
groups | grep -q "ALU_FP_A3" 


if [ $? -eq 0 ]; then 
    echo "You are a Alumno User" 
    prof=2 
fi 

groups | grep -q "Docente_A3" 

if [ $? -eq 0 ]; then 
    echo "You are a Docente User"
    prof=1
else
    echo "You are a Default User"
    prof=0
fi

# if [ $prof -eq 0 ]; then
#     touch .prof0
# elif [ $prof -eq 1 ]; then
#     touch .prof1
# elif [ $prof -eq 2 ]; then
#     touch .prof2
# fi

export USUARIO_TIPO="$prof"