#!bin/bash

docker volume create mysql
docker volume create mysql_config

docker network create mysqlnet

docker run --rm -d -v mysql:/var/lib/mysql \
-v mysql_config:/etc/mysql -p 3306:3306 \
--network mysqlnet \
--name mysqldb \
-e MYSQL_ROOT_PASSWORD=test \
mysql

# docker exec -ti mysqldb bash
docker exec -i mysqldb sh -c 'exec mysql -uroot -p"test"' < ./accounts.sql

echo " mysql succes"

cd dash_board_app

docker build --tag dashboard .

docker run --publish 5000:5000 dashboard
