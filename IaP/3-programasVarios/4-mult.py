numero = int(input("Introduce un número entero del 1 al 10: "))

if numero < 1 or numero > 10:
    print("Error: el número debe estar entre 1 y 10")
else:
    print("Tabla de multiplicar del", numero)

    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)