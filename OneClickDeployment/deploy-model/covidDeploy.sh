#!/bin/bash
current_dir=$(pwd)
echo "current_dir is $current_dir"
parentdir="$(dirname "$current_dir")"
modeldir="$(dirname "$parentdir")"

echo "model dir  is $modeldir and path is $modeldir/agro-cd/app.yaml"
kubectl create namespace argocd
kubectl apply -n argocd -f $modeldir/argo-cd/install.yaml
kubectl apply -n argocd -f $modeldir/argo-cd/app.yaml