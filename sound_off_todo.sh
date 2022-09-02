#!/usr/bin/env sh

echo "bash"
./projects/bash/hello_world.sh
printf "\n"


echo "c"
./projects/c/a.out
printf "\n"


echo "cpp"
./projects/cpp/a.out
printf "\n"


echo "golang"
./projects/golang/main
printf "\n"


echo "javascript"
unset NODE_OPTIONS
node projects/javascript/index.js
printf "\n"


echo "python"
python3 projects/python/hello_world.py
printf "\n"


echo "rust"
./projects/rust/main
printf "\n"


echo "typescript"
#unset NODE_OPTIONS
node projects/typescript/index.ts
printf "\n"


echo "zsh"
./projects/zsh/hello_world.sh
printf "\n"
