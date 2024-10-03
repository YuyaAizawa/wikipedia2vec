#!/bin/bash
cd $(cd $(dirname $0); pwd)/..

docker build -t wikipedia2vec -f docker/Dockerfile .
