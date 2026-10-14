---
title: "Tarea 4: Cifrado simétrico"
author: "Hector V."
date: "30.9.2026"
subject: "SAD"
titlepage: true
titlepage-rule-height: 0
titlepage-background: 0-Template/portada.jpg
toc-own-page: true
titlepage-text-color: ffffff
---


# 1. Crea un fichero de texto con un mensaje.

Hacemos un `touch` para crear el fichero

![Imagen](4-gpg/Nueva\ carpeta/1.png) 

Y luego le introducimos nuestro contenido ultrasecreto

![Imagen](4-gpg/Nueva\ carpeta/1.5.png) 

# 2. Utiliza la orden correspondiente para encriptarlo con cifrado simétrico, sin utilizar parámetros.

Usamos `gpg -d` que es la opcion para encriptar un fichero, se nos es requerida una contraseña, contraseña la cual deberemos guardar para poder desencriptarlo posteriormente

![Imagen](4-gpg/Nueva\ carpeta/2.png) 

# 3. Comprueba de qué tipo es el fichero que se ha generado (binario o de texto)

Es un fichero binario de tipo .gpg, no legible mediante `cat`

![Imagen](4-gpg/Nueva\ carpeta/3.png) 

# 4. Utiliza el comando correspondiente para desencriptar el fichero. ¿El resultado se guarda en algún fichero?

No, el fichero por defecto no se guara en ningun fichero, pero puedes probar con la opcion -o

![Imagen](4-gpg/Nueva\ carpeta/3.1.png) 



# 5. Vuelve a realizar el paso 2, pero en este caso asegúrate de que el fichero encriptado se guarda en un fichero de texto

Con la opcion `-o` (Output) podemos indicar un archivo como salida

![Imagen](4-gpg/Nueva\ carpeta/4.png) 

# 6. Haz una captura del contenido de dicho fichero

![Imagen](4-gpg/Nueva\ carpeta/5.png)