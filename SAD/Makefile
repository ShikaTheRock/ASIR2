PANDOC := pandoc

FONT := DejaVu Sans
TEMPLATE_DIR := 0-Template
TEMPLATE := $(TEMPLATE_DIR)/eisvogel.latex
PORTADA := $(TEMPLATE_DIR)/portada.jpg
WATERMARK := $(TEMPLATE_DIR)/watermark.jpg

AUTHOR := Hector V.

# Nombre de la carpeta donde está este Makefile
SUBJECT := $(notdir $(CURDIR))

# Segundo argumento de make:
# make nuevo Trabajo1
# make pdf Trabajo1
NOMBRE := $(word 2,$(MAKECMDGOALS))

.PHONY: help nuevo pdf clean

help:
	@echo "Uso:"
	@echo "  make nuevo Trabajo1   - Crea un nuevo trabajo"
	@echo "  make pdf Trabajo1     - Convierte todos los Markdown a PDF"
	@echo "  make clean Trabajo1   - Elimina los PDFs"


nuevo:
	@if [ -z "$(NOMBRE)" ]; then \
		echo "Error: falta el nombre del trabajo."; \
		echo "Ejemplo: make nuevo Trabajo1"; \
		exit 1; \
	fi
	@if [ -d "$(NOMBRE)" ]; then \
		echo "Error: la carpeta $(NOMBRE) ya existe."; \
		exit 1; \
	fi

	mkdir -p "$(NOMBRE)"

	@echo '---' > "$(NOMBRE)/$(NOMBRE).md"
	@echo 'title: "$(NOMBRE)"' >> "$(NOMBRE)/$(NOMBRE).md"
	@echo 'author: "$(AUTHOR)"' >> "$(NOMBRE)/$(NOMBRE).md"
	@echo 'date: "'$$(date +%-d.%-m.%Y)'"' >> "$(NOMBRE)/$(NOMBRE).md"
	@echo 'subject: "$(SUBJECT)"' >> "$(NOMBRE)/$(NOMBRE).md"
	@echo 'titlepage: true' >> "$(NOMBRE)/$(NOMBRE).md"
	@echo 'titlepage-rule-height: 0' >> "$(NOMBRE)/$(NOMBRE).md"
	@echo 'titlepage-background: $(PORTADA)' >> "$(NOMBRE)/$(NOMBRE).md"
	@echo 'toc-own-page: true' >> "$(NOMBRE)/$(NOMBRE).md"
	@echo 'titlepage-text-color: ffffff' >> "$(NOMBRE)/$(NOMBRE).md"

	@if [ -f "$(WATERMARK)" ]; then \
		echo 'page-background: ../$(WATERMARK)' >> "$(NOMBRE)/$(NOMBRE).md"; \
	fi

	@echo '---' >> "$(NOMBRE)/$(NOMBRE).md"

	@echo "Trabajo creado: $(NOMBRE)/$(NOMBRE).md"


pdf:
	@if [ -z "$(NOMBRE)" ]; then \
		echo "Error: falta el nombre del trabajo."; \
		echo "Ejemplo: make pdf Trabajo1"; \
		exit 1; \
	fi

	@if [ ! -d "$(NOMBRE)" ]; then \
		echo "Error: la carpeta $(NOMBRE) no existe."; \
		exit 1; \
	fi

	@for file in "$(NOMBRE)"/*.md; do \
		[ -e "$$file" ] || continue; \
		output="$${file%.md}.pdf"; \
		echo "Convirtiendo $$file -> $$output"; \
		cd "$(CURDIR)" && \
		$(PANDOC) "$$file" \
			--template="$(TEMPLATE)" \
			--pdf-engine=xelatex \
			-V mainfont="Noto Sans" \
			-V monofont="Noto Sans Mono" \
			-o "$$output"; \
	done


clean:
	@if [ -z "$(NOMBRE)" ]; then \
		echo "Error: falta el nombre del trabajo."; \
		exit 1; \
	fi
	rm -rf "$(NOMBRE)"


# Hace que make ignore los argumentos que pasamos
%:
	@:
