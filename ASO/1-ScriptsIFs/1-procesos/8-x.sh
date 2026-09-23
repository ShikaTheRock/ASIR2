#!/bin/bash -x

if [ $USUARIO_TIPO -eq 1 ] && [ "$XDG_CURRENT_DESKTOP" = "KDE" ]; then

    # Activar modo presentación
    echo "Activando modo presentación..."
    qdbus6 | grep -i power

    # Preguntar si desea pasar lista
    if kdialog --yesno "¿Desea pasar lista?"; then
        echo "Pasando lista..."
    fi

fi

