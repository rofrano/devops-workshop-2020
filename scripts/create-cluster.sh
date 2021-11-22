#!/bin/bash
echo "Creating Kubernetes cluster with K3D..."
k3d registry create registry.localhost --port 50000
k3d cluster create devops  --agents 1 --registry-use k3d-registry.localhost:50000 --port '8080:80@loadbalancer'
echo "Complete."