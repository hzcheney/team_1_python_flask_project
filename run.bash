#!bin/bash

docker volume create mysql
docker volume create mysql_config

docker network create mysqlnet

docker run --rm -d -v mysql:/var/lib/mysql \
-v mysql_config:/etc/mysql -p 3306:3306 \
--network mysqlnet \
--name mysqldb \
-e MYSQL_ROOT_PASSWORD=test \
mysql:5.7

# docker exec -ti mysqldb bash
docker exec -i mysqldb sh -c 'exec mysql -uroot -p"test"' < ./accounts.sql

echo " mysql succes"

cd dash_board_app

docker build --tag dashboard .

 docker run \
  --rm  \
  --network mysqlnet \
  --name flask_container \
  -p 5000:5000 \
  dashboard