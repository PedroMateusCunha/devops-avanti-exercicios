#!/bin/bash
MICROSERVICE="cep-python-base"
VERSION="v1.0.1"

docker build -t ${MICROSERVICE}:latest -t ${MICROSERVICE}:${VERSION} --build-arg APP_NAME=${MICROSERVICE} --build-arg ENV_NAME=dev cep_python_flask
docker tag ${MICROSERVICE}:${VERSION} ${USER}/${MICROSERVICE}:${VERSION}
docker tag ${MICROSERVICE}:latest ${USER}/${MICROSERVICE}:latest
docker push ${DOCKER_HUB_USER}/${MICROSERVICE}:${VERSION}
docker push ${DOCKER_HUB_USER}/${MICROSERVICE}:latest
