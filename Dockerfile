FROM golang:1.17-bullseye

# Install Python, Node, TypeScript
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
	&& npm install -g npm@latest \
    && npm install typescript -g

ENV PATH="/root/.cargo/bin:${PATH}"

# Install Python

# Install Node

# Install TypeScript


# Install Rust
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y

# Install zsh
RUN apt-get install zsh -y

# Copy project files
WORKDIR /hello_world
COPY projects projects
COPY compile.sh .
COPY sound_off.sh .

CMD ["./sound_off.sh"]
