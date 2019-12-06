export DOCKER_HOST="ssh://pi@10.10.10.179"
docker-compose up -d --build
unset DOCKER_HOST
