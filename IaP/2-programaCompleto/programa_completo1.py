import math
import sys
from ast import literal_eval
from numbers import Number

print("Porfavor. Introduzca su nombre:")
userName=input()

print(userName, ", Bienvenid@ al programa de la unidad 1.")

print("Porfavor", userName, ", Escriba una cadena de texto:")

frase=input()

long=len(frase)

print("Su cadena tiene un tamaño de ", long, "caracteres")

print("Por Ultimo, ",userName, ", Escriba el radio de su circulo favorito:")


# Gracias a KleinerNull por el codigo en https://www.reddit.com/r/learnpython/comments/474ij9/how_to_accept_only_integer_or_float_inputs/

try:
    area = literal_eval(input('Dame un número, por favor. '))
    if isinstance(area, Number):
        radio = math.sqrt(area / math.pi)
        print("El radio del círculo es:", radio)
    else:
        print('No es un número...')
except ValueError:
    print('No es un número...')