#!/bin/bash

docker network create dockernet
docker build -f Dockerfiles/Dockerfile.py_dollar_shekel -t py-dollar-shekel .
docker build -f Dockerfiles/Dockerfile.py_euro_shekel -t py-euro-shekel .
docker build -f Dockerfiles/Dockerfile.js_dollar_shekel -t js-dollar-shekel .
docker build -f Dockerfiles/Dockerfile.js_euro_shekel -t js-euro-shekel .
docker build -f Dockerfiles/Dockerfile.js_pound_shekel -t js-pound-shekel .
docker build -f Dockerfiles/Dockerfile.js_rupee_shekel -t js-rupee-shekel .
docker build -f Dockerfiles/Dockerfile.js_wan_shekel -t js-wan-shekel .
docker build -f Dockerfiles/Dockerfile.js_yen_shekel -t js-yen-shekel .
docker build -f Dockerfiles/Dockerfile.js_handler -t js-handler .
