#!/bin/bash
app="docker.test"
docker network create mongo-net
docker build -t ${app} . 
docker run -d -p 127.0.0.1:56733:80 \
	--name=${app} \
	-v $PWD:/app ${app} \

docker run -d -p 127.0.0.1:56735:27017 \
	--network mongo-net \
	--name mongo \
	--hostname mongo \
       	mongo:latest

docker network connect mongo-net ${app}
