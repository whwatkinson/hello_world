FROM ubuntu:22.04

RUN apt-get update -y

WORKDIR /usr/project
COPY hello_world .

ENTRYPOINT ["tail", "-f", "/dev/null"]
