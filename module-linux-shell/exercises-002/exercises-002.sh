#!/bin/bash

# Este script é uma resolução para o exercício 002 do módulo de linux e shell

: 'Exercicio 002:
* Faça um script que receba como parâmetro um nome de usuário,verique as informações do 
usuário no arquivo /etc/passwd e verique a quais grupos ele pertence (/etc/group), o 
tamanho do diretório pessoal dele (comando du) e o hash da senha dele (/etc/shadow).

* Adicione e remova usuários para teste (adduser/deluser), salve prints,arquive
'

current_user="${1:-$USER}"

function checkUserIsRoot(){
    if [[ $UID -ne 0 ]]; then
        echo "[ ! ] Este script deve ser executado como root"
        exit 1
    fi
}

function checkUserExist() {
    if ! grep -q "^$1:" /etc/passwd ; then
        echo "[ ! ] O usuário $1 não foi encontrado no arquivo /etc/passwd."
        exit 1
    fi
}

function getUserGroup() {
    local groups=$(grep "$1" /etc/group | cut -d ":" -f1 | tr -s "\n" " ")
    echo "$groups"
}

function getHomeFolderSize() {
    local dir_size=$(du -hs $(grep "^$1" /etc/passwd | cut -d ":" -f 6) 2>/dev/null | awk {'print $1'})
    echo "$dir_size"
}

function getUserPasswordHash() {
    local hash=$(grep "^$1:" /etc/shadow | cut -d ":" -f2)
    echo "$hash"
}

function printTable() {
    printf "%s\n" $(printf "%0.s=" {1..100})
    printf "%20s | %s\n" "User" "$current_user"
    printf "%20s | %s\n" "Groups" "$groups"
    printf "%20s | %s\n" "Directory Size" "$dir_size"
    printf "%20s | %s\n" "Password Hash" "$hash"
    printf "%s\n" $(printf "%0.s=" {1..100})
}

function main() {
    checkUserIsRoot "$current_user"
    checkUserExist "$current_user"
    groups=$(getUserGroup "$current_user")
    dir_size=$(getHomeFolderSize "$current_user")
    hash=$(getUserPasswordHash "$current_user")
    printTable
}

main "$@"