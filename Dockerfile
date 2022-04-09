# pull official base image
FROM python:3.9.6-slim-bullseye

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 \
  PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get install -y wget netcat gcc \
  && apt-get clean

# install python dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

EXPOSE 6800

# run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
