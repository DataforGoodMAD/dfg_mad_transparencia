# pull official base image
FROM postgres:13-alpine

# set working directory
WORKDIR /usr/src/app

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d

