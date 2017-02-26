#!/usr/bin/env bash

docker build -t gcr.io/doit-playground/spanner-writer .

gcloud docker -- push gcr.io/doit-playground/spanner-writer:v1