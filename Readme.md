##Introduction
This project is for checking a website declared in .env 
periodically then via kafka stores response code and response time and also availability of words defined in regex.py over the content of webpage.
in Dev Env it creates multiple hosts for zookeeper, kafka, postgres, consumer and producer.
at deploy time hosts can be replaced with real machines in side of .env file or by partially deploying to several machine.


## Start up program in DEV
1- clone git repository and navigate to its folder

2- execute "docker-compose up -d"

### connect to postgres container
1- docker exec -it postgres bash 
 
2-  psql -h postgres -U PG_USER  -d APIMonitor
password: PG_Password

### run unit test for producer
1- docker exec -it producer bash

2-  python3 ProducerUnitTests.py

### check producer log
1- docker logs -f producer

### check consumer log
1- docker logs -f consumer

## Deploy to prod
based on what is Prod or Sandbox environment consists of

it needs to create all env variables in .env file in host

then in app folder run python3 consumer.py or python3 producer.py

based on the role of host.



