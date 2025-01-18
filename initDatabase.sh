#!/bin/bash

# Step 1: Build the Docker Image
docker build -t local-db-image -f database/dockerfile .