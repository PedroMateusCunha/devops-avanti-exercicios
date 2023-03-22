#!/bin/bash

: 'Exercicio 005:
* Faça um script que receba um IP e procure as portas abertas nesse IP e nos 2 IP anteriores e nos 
2 IP anteriores (nc -vvz e pesquisa nas portas TCP de 1 a 1024, idealmente em hosts que existem). 

* Pesquise endereços na sua rede (pelo menos o seu próprio endereço e seu roteador) ou na Internet, 
salve prints, arquive.
'

ip="$1"
inital_ip=$(echo $ip | awk -F. '{print $1"."$2"."$3"."($4-3)}')

function checkIP(){
    if [[ $(echo $ip | awk -F. '{print $4}') -le 2 || $(echo $ip | awk -F. '{print $4}') -ge 253 ]]; then
        echo "[ ! ] Endereço de IP inválido"
        exit 1
    fi
}

function scanner() {
    echo "[ * ] Escaneando as portas 1-1024 em $inital_ip-$(echo $inital_ip | awk -F. '{print $1"."$2"."$3"."($4+2)}')"

    for i in {1..5}; do
        next_ip=$(echo $inital_ip | awk -F. '{print $1"."$2"."$3"."($4+1)}')
        resultado=$(nc -vvz $next_ip 20-22 2>&1 | grep 'succeeded' | cut -d' ' -f4 | tr -s "\n" " ")
        if [[ ! -z $resultado ]]; then
            echo "[ * ] Portas abertas em $next_ip: $resultado"
        fi
        inital_ip=$next_ip
    done
}

function main() {
    checkIP "$1"
    scanner "$1"
}

main "$1"