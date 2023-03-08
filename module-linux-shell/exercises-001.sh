#!/bin/bash

# Este script é uma resolução para o exercício 001 do módulo de linux e shell

: 'Exercicio 001:
* Faça um script que verique todos os arquivos que tenham permissão 777 num determinado subdiretório
(find pode ser uma boa).

* Se o script encontrar os arquivos deve mostrar o tipo do arquivo(comando file) e o tamanho do arquivo 
(ls -lh) bem como o i-node (ls -i). Se o arquivo tiver mais de um hard link deve incluir um aviso com 
o texto *HARD (ls -l).

* Teste cada uma das condições, salve prints, arquive.
'

directory="$1"

function checkDirectory() {
    if [[ -d $1 ]]; then
        return 0
    else
        echo "[ ! ] O diretório $directory não existe."
        exit 1
    fi
}

function checkArg() {
    if [[ -z "$directory" ]]; then
        directory="$(pwd)"
        echo "[ ! ] Nenhum diretório foi especificado."
        echo "      Substituindo pelo diretório atual: ${directory}"
        echo ""
        return 0
    else
        checkDirectory $1
        return 0
    fi
}

function getFiles() {

    checkArg "$directory"

    files=$(find "$directory" -type f -perm 777)

    if [[ -z "$files" ]]; then
        echo "[ ! ] O diretorio $directory não possui nenhum arquivo com permissões 777."
        exit 0
    else
        for file in $files; do
            echo "=========================="
            printf "%-5s %-10s\n" "Arquivo:" "$file"
            printf "%-7s %-10s\n" "Tipo:" "$(file "$file" | cut -d ':' -f2)"
            printf "%-5s %-10s\n" "Tamanho:" "$(ls -l "$file" | awk '{print $5}')"
            printf "%-8s %-10s\n" "I-node:" "$(ls -i "$file" | awk '{print $1}')"
            printf "%-8s %-10s\n" "Links:" "$(ls -l "$file" | awk '{print $2}')"
            local num_links=$(ls -l "$file" | awk '{print $2}')

            if [[ "$num_links" -gt 1 ]]; then
                echo "[ ! ] Aviso: O arquivo $file possui $num_links links simbólicos do tipo HARD."
                echo "      Confira a saída abaixo:"
                echo "          *HARD $(ls -l $file)"
            fi

        done
        echo "=========================="
    fi
}

getFiles
