DAY=input("Dia de la semana: ")

if DAY.lower() == "sabado" or DAY.lower == "domingo":
    print(f"{DAY} es finde.")
elif DAY.lower() in ["lunes", "martes", "miercoles", "jueves", "viernes"]:
    print(f"{DAY} NO es finde.")
else:
    print("nuh uh")
