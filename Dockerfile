FROM golang:1.17-bullseye

# Install dependencies
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		build-essential \
		cmake \
		ca-certificates \
		git \
		python3 \
		python3-dev \
		python3-pip \
		nodejs \
		npm \
		unzip \
	&& npm install -g npm@latest


WORKDIR /hello_world

COPY projects projects
COPY compile.sh .
COPY sound_off.sh .

CMD ["./sound_off.sh"]
