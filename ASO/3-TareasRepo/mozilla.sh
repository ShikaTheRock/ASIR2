#!/bin/bash

#pacman -Ss firefox

lista=$(pacman -Ss firefox | grep -E '^[^ ]' | cut -d '/' -f 2 | cut -d ' ' -f 1,2)

duplicados=$(printf '%s\n' "${lista[@]}" | sort | uniq -d)

if [[ -n "$duplicados" ]]; then
    echo "Hay duplicados:"
    echo $duplicados
fi

updateNum=$(pacman -Ss firefox | grep "instalado:" | grep firefox | wc -l)
echo "Paquetes por actualizar de firefox: $updateNum"
echo $(pacman -Ss firefox | grep "instalado:" | grep firefox)| while read line; do
    repo=$(echo $line | cut -d '/' -f 1)
    ver=$(echo $line | cut -d ' ' -f 4| cut -d ']' -f 1)
    repoVer=$(echo $line | cut -d ' ' -f 2)
    paquete=$(echo $line | cut -d '/' -f 2)

    echo "$repo - $paquete"
    echo "Esta en la version $ver, cuando la version del repo es: $repoVer"
done

