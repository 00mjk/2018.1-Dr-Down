#!/bin/bash
#
# Purpose: Continuous deploy on staging environment
#
# Author: João Pedro Sconetto <sconetto.joao@gmail.com>

echo $DOCKER_ID_USER_PASSWORD | docker login --username $DOCKER_ID_USER --password-stdin
docker tag 20181drdown_django $DOCKER_ID_USER/20181-dr-down_django
docker push $DOCKER_ID_USER/20181-dr-down_django

sudo apt-get install sshpass -y
sshpass -p $SSH_PASSWORD ssh drdown@104.236.68.6 '/bin/bash /home/drdown/deploy.sh'
