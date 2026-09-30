num=input("Introduzca un numero - ")
if num != 0:
    if num.isnumeric():
        rango=range(1, int(num)+1)
        for op in list(rango):
            if op % 2 == 0:
                print(op)
    else:
        print("Intruduzca un numero!")
else:
    print("El numero no puedeser igual a 0")

    print(range(1,10))