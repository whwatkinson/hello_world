FROM golang:1.17-bullseye

# Install Python, Node, TypeScript
RUN apt-get update

# Install Python
RUN apt-get install -y --no-install-recommends python3

# Install Node
RUN apt-get install -y --no-install-recommends nodejs npm && npm install -g npm@latest

# Install TypeScript
RUN npm install typescript -g

# Install Rust
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Install zsh
RUN apt-get install zsh -y

# Copy project files
WORKDIR /hello_world
COPY projects projects
COPY compile.sh .
COPY sound_off.sh .

CMD ["./sound_off.sh"]
