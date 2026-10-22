sixseven={}

while True:
    print("=== Gestión de Direcciones IP ===")
    print("1. Registrar equipo | 2. Buscar IP | 3. Listar inventario | 4. Salir")

    pepino = input("Opcion: ")

    if pepino == "1":
        donpepito = input("Nombre del host: ")
        donjose = input("Dirección IP: ")
        sixseven[donpepito]=donjose
        print(sixseven)
        print("[OK] Equipo registrado")
    elif pepino == "2":
        reydelostrols = input("Dirección Host a buscar: ")
        print("> IP de", reydelostrols, ": ", sixseven[reydelostrols])
        # print(list(sixseven))
    elif pepino == "3":
        for op in sixseven:
            print(op, "-", sixseven[op])
    elif pepino == "4":
        break
    else:
        print("Non valid option introduced.")