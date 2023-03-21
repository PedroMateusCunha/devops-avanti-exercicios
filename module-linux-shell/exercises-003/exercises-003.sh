#!/bin/bash

# Este script é uma resolução para o exercício 003 do módulo de linux e shell

: 'Exercicio 003:
* Faça um script que localize o arquivo teste-bash-3.cfg em qualquer lugar do sistema de 
arquivos (find), leia o conteúdo desse arquivo e mostre todas as linhas que contenham o sinal 
de igual (grep). Depois faça uma atualização que receba como primeiro parâmetro os valores 
on e off. Caso off seja passado, como parâmetro o comportamento se mantém, mas caso on seja 
mostrado comoparâmetro deve-se mostrar na tela o seguinte texto com os valores de cada linha 
no lugar das indicações abaixo:

* Chave: <valor antes do igual> / Valor: <valor depois do igual>

* Teste o arquivo em diferentes locais, salve prints, arquive
'

file_cfg=""

function printHelp() {
  echo "Uso: bash $0 [opções] [parâmetro]"
  echo "Opções:"
  echo "  -f Arquivo   Determina um arquivo"
  echo "  -k Chave     Determina uma chave"
  echo "  -v Valor     Determina o valor da chave"
  echo ""
  echo "Exemplo:"
  echo "  $0 -f arquivo.cfg -k debug -v on"
  echo ""
}

function searchFile() {

    file_cfg=$(find / -name "$1" -print -quit 2>/dev/null)

    if [[ -z "$file_cfg" ]]; then
        echo "Arquivo $file_cfg não encontrado."
        exit 0
    fi
}


function checkLines() {
    local lines=$(grep '=' "$1" 2>/dev/null)
    if [[ -z $lines  ]]; then 
        echo "Nenhuma linha com sinal de igualdade encontrada"
        exit 0
    fi
}

function cli() {
    while getopts ":f:k:v:h" opt; do
        case $opt in
            f)
                file="$OPTARG"
                ;;
            k)
                key="$OPTARG"
                ;;
            v)
                value="$OPTARG"
                ;;
            h)
                printHelp
                exit 0
                ;;
            \?)
                echo "Opção inválida: -$OPTARG" >&2
                exit 1
                ;;
            :)
                echo "Opção -$OPTARG requer um argumento" >&2
                exit 1
                ;;
        esac
    done

    if [[ -z $file || -z $key || -z $value ]]; then
        echo "Erro: Todos os argumentos são obrigatórios." >&2
        echo ""
        printHelp
        exit 1
    fi
}

function main() {
    cli "$@"
    searchFile "$file"
    checkLines "$file_cfg"
    tmp_file=$(mktemp)
    new_line=$(awk -v key="$key" -v value="$value" -F= '$1==key {$2=value; print $1"="$2} $1!=key {print}' $file_cfg)
    echo "$new_line" > "$tmp_file"
    if [[ -z $(diff $tmp_file $file_cfg) ]]; then
        echo "Nenhuma alteração foi realizada"
    else
        echo ""
        echo "ANTES"
        printf "%s\n" $(printf "%0.s=" {1..50})
        echo "$(cat $file_cfg)"
        echo ""
        echo "DEPOIS"
        printf "%s\n" $(printf "%0.s=" {1..50})
        echo "$(cat $tmp_file)"
        mv $tmp_file $file_cfg
    fi

}

main "$@"