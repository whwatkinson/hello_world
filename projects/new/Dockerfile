FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y

ENV PATH=/usr/lib/$LANG:$PATH

WORKDIR /usr/project
COPY hello_world .

ENTRYPOINT ["tail", "-f", "/dev/null"]
