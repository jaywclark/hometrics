export DOCKER_HOST="ssh://pi@10.10.10.197"
docker-compose up -d --build
docker logs hometrics_meter_1 -f -t
unset DOCKER_HOST
