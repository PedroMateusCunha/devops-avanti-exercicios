#!/bin/bash
MICROSERVICE="cep-python-base"
VERSION="v1.0.2"

[ -z $DOCKER_HUB_USER ] && exit 1
echo ${DOCKER_HUB_USER}

docker build -t ${MICROSERVICE}:latest -t ${MICROSERVICE}:${VERSION} --build-arg APP_NAME=${MICROSERVICE} --build-arg ENV_NAME=dev --no-cache cep_python_flask
docker tag ${MICROSERVICE}:${VERSION} ${DOCKER_HUB_USER}/${MICROSERVICE}:${VERSION}
docker tag ${MICROSERVICE}:latest ${DOCKER_HUB_USER}/${MICROSERVICE}:latest
docker push ${DOCKER_HUB_USER}/${MICROSERVICE}:${VERSION}
docker push ${DOCKER_HUB_USER}/${MICROSERVICE}:latest
