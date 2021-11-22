#!/bin/bash
echo "Deleting Kubernetes cluster..."
k3d cluster delete devops
k3d registry delete registry.localhost
echo "Complete."