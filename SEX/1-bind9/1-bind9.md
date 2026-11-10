---
title: "1 - Tarea DNS: BIND9"
author: "Hector V."
date: "3.11.2026"
subject: "SEX"
titlepage: true
titlepage-rule-height: 0
titlepage-background: 0-Template/portada.jpg
toc-own-page: true
titlepage-text-color: ffffff
---

# Práctica: instalación y configuración de un servidor DNS con BIND9

## 1. Introducción

En esta práctica he instalado y configurado un servidor DNS utilizando BIND9 en Ubuntu Server. Para comprobar su funcionamiento he utilizado una segunda máquina con Linux Mint, conectada a la misma red.

El objetivo es poder resolver nombres de equipos del dominio `asir2.test` y también realizar consultas inversas, es decir, obtener el nombre de un equipo a partir de su dirección IP.

## 2. Entorno de trabajo

Para realizar la práctica he utilizado dos máquinas virtuales conectadas a una red interna.

| Máquina | Sistema operativo | Dirección IP |
|---|---|---|
| Servidor DNS | Ubuntu Server | 192.168.3.10 |
| Cliente | Linux Mint | 192.168.3.100 |

La máscara de red utilizada es `255.255.255.0`, por lo que la red es `192.168.3.0/24`.

He utilizado el dominio `asir2.test`. Además, he creado algunos nombres de ejemplo para poder probar los distintos registros DNS:

| Nombre | Dirección IP | Uso |
|---|---|---|
| dns1.asir2.test | 192.168.3.10 | Servidor DNS |
| web1.asir2.test | 192.168.3.20 | Servidor web de ejemplo |
| mail1.asir2.test | 192.168.3.30 | Servidor de correo de ejemplo |
| repo.asir2.test | 192.168.3.40 | Servidor de repositorio de ejemplo |

Los tres últimos nombres se utilizan para las pruebas DNS, por lo que no es necesario que existan esas máquinas.

## 3. Instalación de BIND9

Una vez iniciada la máquina Ubuntu Server, he actualizado los repositorios:

```bash
sudo apt update
```

A continuación he instalado BIND9 y las herramientas necesarias para realizar consultas DNS:

```bash
sudo apt install bind9 bind9utils dnsutils -y
```

Para comprobar que el servicio se había iniciado correctamente he utilizado:

```bash
sudo systemctl status bind9
```

El servicio aparece como `active (running)`, por lo que la instalación se ha realizado correctamente.

También he realizado una primera consulta local para comprobar que el servidor DNS responde:

```bash
dig @127.0.0.1 localhost
```

## 4. Configuración de la zona directa

La zona directa se utiliza para traducir nombres de dominio a direcciones IP.

Primero he realizado una copia del archivo de configuración para poder recuperarlo en caso de cometer algún error:

```bash
sudo cp /etc/bind/named.conf.local /etc/bind/named.conf.local.bak
```

Después he abierto el archivo:

```bash
sudo nano /etc/bind/named.conf.local
```

He añadido la declaración de la zona `asir2.test`:

```conf
zone "asir2.test" {
    type master;
    file "/etc/bind/db.asir2.test";
};
```

Una vez declarada la zona, he creado su archivo correspondiente:

```bash
sudo nano /etc/bind/db.asir2.test
```

El contenido utilizado ha sido el siguiente:

```dns
$TTL 86400
@   IN  SOA dns1.asir2.test. admin.asir2.test. (
        2026110301
        3600
        1800
        604800
        86400 )

@       IN  NS      dns1.asir2.test.

dns1    IN  A       192.168.3.10
web1    IN  A       192.168.3.20
mail1   IN  A       192.168.3.30
repo    IN  A       192.168.3.40

www     IN  CNAME   web1.asir2.test.
@       IN  MX 10   mail1.asir2.test.
```

En este archivo he añadido varios tipos de registros:

- **SOA:** indica el servidor principal de la zona y algunos parámetros de configuración.
- **NS:** indica qué servidor DNS tiene autoridad sobre el dominio.
- **A:** relaciona un nombre con una dirección IPv4.
- **CNAME:** crea un alias. En este caso, `www.asir2.test` apunta a `web1.asir2.test`.
- **MX:** indica el servidor encargado de recibir el correo del dominio. El valor `10` es su prioridad.

El número de serie del registro SOA identifica la versión de la zona. Si se modifica el archivo, es necesario aumentarlo.

### 4.1. Comprobación de la zona directa

Antes de recargar el servicio he comprobado que la configuración no tuviera errores:

```bash
sudo named-checkconf
```

El comando no ha mostrado ningún error.

Después he comprobado el archivo de la zona:

```bash
sudo named-checkzone asir2.test /etc/bind/db.asir2.test
```

La comprobación ha terminado correctamente y BIND9 reconoce la zona como válida.

Por último, he recargado el servicio:

```bash
sudo systemctl reload bind9
```

### 4.2. Pruebas de resolución directa

Para comprobar los registros he realizado varias consultas desde Ubuntu Server:

```bash
dig @127.0.0.1 web1.asir2.test A +short
dig @127.0.0.1 dns1.asir2.test A +short
dig @127.0.0.1 www.asir2.test A +short
dig @127.0.0.1 asir2.test MX +short
dig @127.0.0.1 asir2.test NS +short
```

Los resultados obtenidos corresponden con los registros configurados:

| Consulta | Respuesta |
|---|---|
| web1.asir2.test | 192.168.3.20 |
| dns1.asir2.test | 192.168.3.10 |
| www.asir2.test | web1.asir2.test, con IP 192.168.3.20 |
| MX de asir2.test | mail1.asir2.test |
| NS de asir2.test | dns1.asir2.test |

Con estas consultas he comprobado que los registros de la zona directa se resuelven correctamente.

## 5. Configuración de la zona inversa

La zona inversa permite realizar la consulta al revés: a partir de una dirección IP se obtiene el nombre asociado.

Como la red utilizada es `192.168.3.0/24`, el nombre de la zona inversa es:

```text
3.168.192.in-addr.arpa
```

He vuelto a editar el archivo de configuración:

```bash
sudo nano /etc/bind/named.conf.local
```

Y he añadido la siguiente zona:

```conf
zone "3.168.192.in-addr.arpa" {
    type master;
    file "/etc/bind/db.192.168.3";
};
```

A continuación he creado el archivo de la zona inversa:

```bash
sudo nano /etc/bind/db.192.168.3
```

He introducido estos registros:

```dns
$TTL 86400
@   IN  SOA dns1.asir2.test. admin.asir2.test. (
        2026110301
        3600
        1800
        604800
        86400 )

@       IN  NS      dns1.asir2.test.

10      IN  PTR     dns1.asir2.test.
20      IN  PTR     web1.asir2.test.
30      IN  PTR     mail1.asir2.test.
40      IN  PTR     repo.asir2.test.
```

En este caso he utilizado registros `PTR`, que relacionan cada dirección IP con su nombre correspondiente. Por ejemplo, el registro `20` corresponde a la dirección `192.168.3.20`.

### 5.1. Comprobación de la zona inversa

He comprobado de nuevo la configuración general:

```bash
sudo named-checkconf
```

Y después la zona inversa:

```bash
sudo named-checkzone 3.168.192.in-addr.arpa /etc/bind/db.192.168.3
```

La comprobación ha sido correcta, así que he recargado BIND9:

```bash
sudo systemctl reload bind9
```

Para comprobar la resolución inversa he utilizado:

```bash
dig @127.0.0.1 -x 192.168.3.20 +short
```

La respuesta devuelta es:

```text
web1.asir2.test.
```

Por tanto, la consulta inversa también funciona.

## 6. Permitir consultas desde Linux Mint

Hasta este punto las consultas se habían realizado desde el propio servidor. Para poder utilizar el DNS desde Linux Mint he tenido que permitir las consultas desde la red local.

En Ubuntu Server he editado el archivo:

```bash
sudo nano /etc/bind/named.conf.options
```

Dentro del bloque `options` he dejado configuradas estas opciones:

```conf
listen-on { 127.0.0.1; 192.168.3.10; };
listen-on-v6 { ::1; };
allow-query { localhost; 192.168.3.0/24; };
recursion no;
```

Con esto BIND9 escucha en la dirección del servidor y permite consultas desde los equipos de la red `192.168.3.0/24`. La recursión está desactivada porque en esta práctica se utiliza el servidor para responder por su propia zona.

He comprobado la configuración y reiniciado el servicio:

```bash
sudo named-checkconf
sudo systemctl restart bind9
sudo systemctl status bind9
```

El servicio se ha iniciado correctamente.

También he comprobado el estado del cortafuegos:

```bash
sudo ufw status
```

En caso de tener UFW activo, es necesario permitir el puerto 53 para UDP y TCP:

```bash
sudo ufw allow from 192.168.3.0/24 to any port 53 proto udp
sudo ufw allow from 192.168.3.0/24 to any port 53 proto tcp
```

## 7. Configuración y pruebas desde Linux Mint

En la máquina Linux Mint he configurado la conexión de red con los siguientes datos:

| Parámetro | Valor |
|---|---|
| Dirección IP | 192.168.3.100 |
| Máscara | 255.255.255.0 |
| Servidor DNS | 192.168.3.10 |

Una vez aplicada la configuración, he comprobado que el cliente puede comunicarse con Ubuntu Server:

```bash
ping -c 4 192.168.3.10
```

Después he realizado las consultas DNS desde Linux Mint, indicando la dirección del servidor para asegurarme de que las peticiones se envían al BIND9 configurado:

```bash
nslookup web1.asir2.test 192.168.3.10
dig @192.168.3.10 www.asir2.test A +short
dig @192.168.3.10 asir2.test MX +short
dig @192.168.3.10 asir2.test NS +short
dig @192.168.3.10 -x 192.168.3.20 +short
```

Las consultas devuelven los mismos registros que se habían comprobado desde Ubuntu Server. De esta forma he verificado que el cliente puede utilizar el servidor DNS a través de la red.

## 8. Añadir un nuevo servidor

Como última parte he añadido el nombre `repo.asir2.test`, asociado a la dirección `192.168.3.40`.

Para ello he editado el archivo de la zona directa:

```bash
sudo nano /etc/bind/db.asir2.test
```

Y he añadido el registro:

```dns
repo    IN  A    192.168.3.40
```

Después he abierto el archivo de la zona inversa:

```bash
sudo nano /etc/bind/db.192.168.3
```

He añadido el registro PTR correspondiente:

```dns
40      IN  PTR  repo.asir2.test.
```

Al modificar los archivos de zona he actualizado también el número de serie del SOA.

Por último, he vuelto a validar los archivos:

```bash
sudo named-checkzone asir2.test /etc/bind/db.asir2.test
sudo named-checkzone 3.168.192.in-addr.arpa /etc/bind/db.192.168.3
sudo named-checkconf
```

Como las comprobaciones no han mostrado errores, he recargado el servicio:

```bash
sudo systemctl reload bind9
```

He comprobado el nuevo registro con estas consultas:

```bash
dig @192.168.3.10 repo.asir2.test A +short
dig @192.168.3.10 -x 192.168.3.40 +short
```

La resolución directa devuelve `192.168.3.40` y la inversa devuelve `repo.asir2.test`.

## 9. Conclusión

Con esta práctica he conseguido instalar BIND9 en Ubuntu Server y configurar un servidor DNS para la red `192.168.3.0/24`.

He creado una zona directa con registros A, CNAME, MX y NS, y otra inversa con registros PTR. También he configurado Linux Mint para realizar consultas al servidor.

Las pruebas realizadas han permitido comprobar que los nombres configurados se resuelven tanto desde Ubuntu Server como desde el equipo cliente.
