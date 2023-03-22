#!/bin/bash

: 'Exercicio 006:
* Faça um script que interprete o seguinte arquivo de texto (próximoslide, esquerda) e crie um JSON 
baseado no conteúdo do arquivo detexto (próximo slide, direita). Não se preocupe com as 
vírgulasadicionais nem em quebrar as linhas da melhor forma.Teste incluindo e removendo blocos, 
salve prints, arquive.
'

function printHelp() {
  echo "Uso: bash $0 [arquivo]"
  echo ""
  echo "Exemplo:"
  echo "    bash $0 file.cfg"
  echo ""
}

function main() {

    if [[ -z $1 ]]; then
            echo "Erro: É necessário indicar um arquivo de texto" >&2
            echo ""
            printHelp
            exit 1
    fi

    echo "{"
    open=0
    while read line; do
            if [[ $(echo $line | cut -c 1) = "[" ]]; then
                let open+=1
                echo "   { \"$(echo $line | tr -d "[]")\": "
            else
                if [[ $open -ne 0  ]]; then
                    echo "      { \"$(echo $line | cut -d'=' -f1)\":\"$(echo $line | cut -d'=' -f2)\" },}"
                    let open-=1
                else
                    echo "      { \"$(echo $line | cut -d'=' -f1)\":\"$(echo $line | cut -d'=' -f2)\" },"
                fi
            fi
    done <<< "$(grep -v "^#" $1)"
    echo "}"
}

main "$1"