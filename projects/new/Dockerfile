# Not a project but here as a stub for a new project
# cp -r projects/new projects/$NAME

FROM ubuntu:22.04

RUN apt-get update -y

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /usr/lib
ENV PATH=/usr/lib/$LANG:$PATH

WORKDIR /usr/project
COPY hello_world .

ENTRYPOINT ["tail", "-f", "/dev/null"]
