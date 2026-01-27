#!/bin/bash
set -e

echo "Building with Docker..."
docker build -t bg-remover .
docker run -p 8080:8080 bg-remover
