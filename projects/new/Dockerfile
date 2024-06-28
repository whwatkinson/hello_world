FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y \
    ...

WORKDIR /usr/lib
ENV PATH=/usr/lib/$LANG:$PATH

WORKDIR /usr/project
COPY hello_world .
COPY run.sh .
RUN chmod +x run.sh

#CMD ["./run.sh"]
ENTRYPOINT ["tail", "-f", "/dev/null"]
