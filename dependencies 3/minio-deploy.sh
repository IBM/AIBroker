#!/bin/bash

oc apply -f minio/minio-ns.yml
oc apply -f minio/minio-pvc.yml
oc apply -f minio/minio-deployment.yml
oc apply -f minio/minio-service.yml
oc apply -f minio/minio-route.yml
