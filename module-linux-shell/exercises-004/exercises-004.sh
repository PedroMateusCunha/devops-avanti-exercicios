#!/bin/bash

: 'Exercicio 004:
* Faça um script que mostre o momento que rodou (comando date), a quanto tempo o servidor estava 
ligado quando isso aconteceu(uptime) e quais usuários estavam logados no momento (comando w). 

*Também mostre a quantidade de memória disponível (free) e aquantidade de espaço na raiz do sistema 
de arquivos (df).Adicione e remova usuários para teste (adduser/deluser), salve prints,arquive.
'

function printDate() {
    local date="$1"
    printf "%-6s %15s %s\n" "[INFO]" "Data: " "$(echo $date | awk '{print $1"/"$2"/"$3}')"
    printf "%-6s %15s %s\n" "[INFO]" "Hora: " "$(echo $date | awk '{print $4}')"
}

function printUpTime() {
    local uptime="$1"
    printf "%-6s %15s %s\n" "[INFO]" "Uptime: " "$uptime"
}

function printInfo() {
    local users="$1"
    printf "\n%15s | %s\n" "Logged Users" "TTY"
    printf "%s\n" $(printf "%0.s=" {1..25})

    while read user; do
        username=$(echo "$user" | awk '{print $1}')
        tty=$(echo "${user}" | awk '{print $2}')
        printf "%15s | %s\n" "$username" "$tty"
    done <<< "$users"   
}

function printMemoryFree() {
    local memory_free="$1"
    printf "%-6s %15s %s\n" "[INFO]" "Memory Free: " "$memory_free"
}

function printDiskFree() {
    local disk_free="$1"
    printf "%-6s %15s %s\n" "[INFO]" "Disk Free: " "$disk_free"
}

function main() {
    date=$(echo "$(date "+%d %m %Y %H:%M:%S")")
    uptime=$(uptime | awk '{print $3}' | tr -s "," " ")
    users=$(w -hs)
    memory_free=$(free -ht --giga | awk '{print $4}' | sed -n '2p')
    disk_free=$(df -h ~ | awk '{print $4}' | sed -n '2p')
    printDate "$date"
    printUpTime "$uptime"
    printMemoryFree "$memory_free"
    printDiskFree "$disk_free"
    printInfo "$users"
}

main