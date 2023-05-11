#!/bin/bash

CEP_LIST=("64260000" "63260000" "62260000")

for cep in "${CEP_LIST[@]}"; do
    response=$(curl -s -I -o /dev/null -w "%{http_code}" http://"$(minikube ip)":5000/quest/${cep})
    if [[ "$response" =~ ^2 ]]; then
    echo "CEP: $cep - Requisição bem sucedida (código $response)"
  else
    echo "CEP: $cep - Erro na requisição (código $response)"
  fi

done

echo -e "\nLista de CEPs em CSV:\n"
curl -s http://"$(minikube ip)":5000/list_csv
