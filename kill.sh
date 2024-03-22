#!/bin/bash
app="docker.test"
docker kill $app 
docker remove $app 

docker kill mongo
docker remove mongo
docker network rm mongo-net
