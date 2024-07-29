#!/bin/bash
app="docker.test"
docker network create mongo-net --subnet=192.168.240.0/24
docker build -t ${app} .
docker run -d -p 127.0.0.1:56733:80 \
	--name=${app} \
	-v $PWD:/app ${app} \

docker run -d -p 127.0.0.1:56735:27017 \
	--network mongo-net \
	--name mongo \
	--hostname mongo \
       	-v /var/www/database:/database mongo

docker network connect mongo-net ${app}
