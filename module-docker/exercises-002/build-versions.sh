#!/bin/bash

DOCKERFILE="Dockerfile"
CONTEXT_DIR="cep_python_flask"
DOCKERFILE_PATH="${CONTEXT_DIR}/${DOCKERFILE}"

while read line; do
    MICROSERVICE=$(echo $line | cut -d "=" -f 1)
    VERSION=$(echo $line | cut -d "=" -f 2)

    docker build -t ${MICROSERVICE}:latest \
        -t ${MICROSERVICE}:${VERSION} \
        --build-arg APP_NAME=${MICROSERVICE} \
        --build-arg ENV_NAME=dev \
        --build-arg VERSION=${VERSION} \
        ${CONTEXT_DIR} \
        -f ${DOCKERFILE_PATH}

done <versions.txt
