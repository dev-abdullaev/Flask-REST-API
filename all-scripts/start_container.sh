#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull 2303073/simple-python-flask-app

# Run the Docker image as a container
docker run -d -p 8080:8080 2303073/simple-python-flask-app
