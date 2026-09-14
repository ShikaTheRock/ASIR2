---
title: "1-MarkdownHTML"
author: "Hector V."
date: "11.9.2026"
subject: "IAW"
titlepage: true
titlepage-rule-height: 0
titlepage-background: 0-Template/portada.jpg
toc-own-page: true
titlepage-text-color: ffffff
---

# Protocolo HTTP

## 1. ¿Qué es HTTP?

**HTTP** (*HyperText Transfer Protocol*) es un protocolo de comunicación utilizado para transferir recursos en la Web. Funciona mediante mensajes de **petición** y **respuesta** entre un cliente y un servidor.

---

## 2. Arquitectura cliente-servidor

- **Cliente:** normalmente un navegador que solicita un recurso.
- **Servidor:** recibe la petición, la procesa y devuelve una respuesta.
- **Recurso:** puede ser una página HTML, una imagen, un archivo o datos.

Ejemplo sencillo:

```text
Cliente → petición HTTP → Servidor
Cliente ← respuesta HTTP ← Servidor
```

Una URL de ejemplo es `http://localhost`.

## 3. ¿Cómo funciona una petición HTTP?

De forma simplificada:

1. El cliente solicita un recurso.
2. El servidor recibe y procesa la petición.
3. El servidor devuelve una respuesta.
4. El cliente interpreta la respuesta y muestra el resultado.

Ejemplo de petición:

```http
GET /index.html HTTP/1.1
Host: ejemplo.com
Accept: text/html
```

Ejemplo de respuesta:

```http
HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hola</h1>
```

Las cabeceras proporcionan información adicional sobre la petición o la respuesta.

## 4. Métodos HTTP

| Método | Uso |
|---|---|
| `GET` | Obtener un recurso. |
| `POST` | Enviar datos para su procesamiento. |
| `PUT` | Reemplazar un recurso. |
| `PATCH` | Modificar parcialmente un recurso. |
| `DELETE` | Eliminar un recurso. |
| `HEAD` | Obtener información de una respuesta sin su contenido. |
| `OPTIONS` | Consultar las opciones de comunicación disponibles. |


## 5. Códigos de estado

El servidor utiliza códigos de tres cifras para indicar el resultado de una petición.

| Código | Significado | Ejemplo |
|---|---|---|
| `200` | Correcto | La petición se ha realizado correctamente. |
| `201` | Creado | Se ha creado un nuevo recurso. |
| `301` | Redirección permanente | El recurso tiene una nueva ubicación. |
| `400` | Petición incorrecta | La petición tiene un error. |
| `401` | No autorizado | Se necesita autenticación. |
| `403` | Prohibido | El acceso no está permitido. |
| `404` | No encontrado | El recurso no existe. |
| `500` | Error del servidor | El servidor ha encontrado un problema. |

Las familias principales son:

- **1xx:** información.
- **2xx:** éxito.
- **3xx:** redirección.
- **4xx:** errores del cliente.
- **5xx:** errores del servidor.

## 6. Historia de HTTP

HTTP fue desarrollado por **Tim Berners-Lee** durante la creación de la World Wide Web entre 1989 y 1991.

Su evolución principal fue:

1. **HTTP/0.9:** versión inicial y muy sencilla, con el método `GET`.
2. **HTTP/1.0:** añadió cabeceras y códigos de estado.
3. **HTTP/1.1:** mejoró las conexiones y se convirtió en un estándar ampliamente utilizado.
4. **HTTP/2:** mejoró el rendimiento y la gestión de múltiples recursos.
5. **HTTP/3:** utiliza QUIC para mejorar el transporte de las comunicaciones.

## 7. Ventajas de HTTP

- Es sencillo y extensible.
- Permite comunicar clientes y servidores de forma estandarizada.
- Puede transportar diferentes tipos de recursos.
- Utiliza métodos y códigos de estado que facilitan la comunicación.

## 8. Enlaces y recursos

- [MDN Web Docs - HTTP](https://developer.mozilla.org/es/docs/Web/HTTP)
- [IETF - RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html)
- [MDN - Evolución de HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/Evolution_of_HTTP)
- [Otro documento local](./otro-documento.md)

### Imagen

![Esquema](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_TymoAM5rNO3skbSFNV_jw6dVN_jfSxQxZSSO6gP9kg&s=10)

## 9. Fuentes

1. Mozilla Developer Network (MDN), documentación de HTTP.
2. Internet Engineering Task Force (IETF), **RFC 9110 - HTTP Semantics**.
3. Mozilla Developer Network (MDN), **Evolución de HTTP**.
