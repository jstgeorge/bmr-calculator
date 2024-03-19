#!/bin/bash

# Build the Docker image
docker build -t bmr_calculator .

# Run the Docker container with Docker-in-Docker
docker run -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 bmr_calculator