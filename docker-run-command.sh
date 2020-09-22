#!/bin/bash

DOCKER_MACHINE_ID=`docker ps | grep django-interview_web | awk '{print $1}'`
echo "Running command '$1' in docker machine $DOCKER_MACHINE_ID"

docker exec -it $DOCKER_MACHINE_ID "$@"
