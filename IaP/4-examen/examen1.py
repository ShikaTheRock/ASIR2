# tuplas - () No son modificables
# Sets - [] Son como los arrays
# Diccioonarios - {campo: valor}
SISTEMA = ("admin", "sysadmin123", "Angel")
Intentos=3
while Intentos > 0:
    print("=== Control de Acceso al Servidor ===")
    user = input("Usuario:")
    passw = input("Contraseña:")

    if user == SISTEMA[0]:
        if passw == SISTEMA[1]:
            print("[OK] Bienvenido, ",SISTEMA[2],".")
            break
        else:
            print("Mal Password")
            Intentos=Intentos-1
    else:
        print("Mal User")
        Intentos=Intentos-1