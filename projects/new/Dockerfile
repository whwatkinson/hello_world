FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y

WORKDIR /usr/project
COPY hello_world .

ENTRYPOINT ["tail", "-f", "/dev/null"]
