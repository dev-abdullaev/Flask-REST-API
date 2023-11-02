#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull 2303073/simple-python-flask-app

# Run the Docker image as a container
docker-compose -f local.yml up -d