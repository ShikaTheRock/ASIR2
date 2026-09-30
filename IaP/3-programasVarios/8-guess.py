numero_secreto = 7

numero = int(input("Adivina el número: "))

while numero != numero_secreto:
    numero = int(input("Incorrecto. Inténtalo de nuevo: "))

print("¡Correcto!")