---
title: "1-Guía rápida: usar dos PDF como fondos con Eisvogel"
author: "Hector V."
date: "10.9.2026"
subject: "PI"
titlepage: true
titlepage-rule-height: 0
titlepage-background: "/home/shika/ASIR2/PI/0-Template/portada.jpg"
toc-own-page: true
titlepage-text-color: ffffff
---



Portada en la primera página y fondo en el resto del documento

Objetivo. Configurar Eisvogel para usar un PDF como fondo de la portada y otro PDF como fondo de todas las páginas restantes, usando Pandoc + XeLaTeX.

1. Estructura de carpetas
```
PI/
├── .pandoc/templates/eisvogel.latex
├── 0-Template/
│   ├── portada.pdf      ← fondo de la portada
│   └── fondo.pdf        ← fondo del resto de páginas
├── 1-Markdown/
│   └── 1-Markdown.md
└── Makefile
```
2. Configurar el Markdown

En el YAML inicial del Markdown, indica ambos PDF:
```yaml
---
title: "1-Markdown"
author: "Hector V."
date: "10.9.2026"
subject: "PI"
titlepage: true
titlepage-rule-height: 0
titlepage-background: "/ruta/absoluta/PI/0-Template/portada.pdf"
toc-own-page: true
titlepage-text-color: ffffff
page-background: "/ruta/absoluta/PI/0-Template/fondo.pdf"
---
```
3. Por qué usar rutas absolutas

Las rutas relativas como ../0-Template/portada.pdf pueden fallar al compilar con LaTeX. La solución práctica es generar en el Markdown la ruta absoluta del archivo.

realpath 0-Template/portada.pdf

4. Hacerlo automático en el Makefile

Define las rutas a partir de la carpeta donde está el Makefile:

PORTADA := $(CURDIR)/0-Template/portada.pdf
FONDO   := $(CURDIR)/0-Template/fondo.pdf

Al crear el Markdown, escribe las variables en el YAML:

@echo 'titlepage-background: "$(PORTADA)"' >> "$(NOMBRE)/$(NOMBRE).md"
@echo 'page-background: "$(FONDO)"' >> "$(NOMBRE)/$(NOMBRE).md"

5. Convertir a PDF
```bash
$(PANDOC) "$${file}" \
    --template=eisvogel \
    --pdf-engine=xelatex \
    -o "$${output}"
```
No hace falta modificar Eisvogel: el template ya usa titlepage-background para la portada y page-background para el resto de páginas.

6. Resultado

Al ejecutar:
```bash
make pdf 1-Markdown
```
se genera 1-Markdown.pdf con portada.pdf en la primera página y fondo.pdf como fondo de las demás páginas.

Nota importante

La forma más sencilla es que portada.pdf y fondo.pdf tengan una sola página. Si un PDF tiene varias páginas, LaTeX normalmente usa la primera página como imagen de fondo. Para un fondo repetido, prepara un PDF de una sola página con el diseño deseado.
