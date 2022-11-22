#!/usr/bin/env bash

./compile.sh
printf "\n\n\n\n\n\n\n"


#echo "bash" > "${VAR}"
echo 'bash projects/bash/hello_world.sh' | "${VAR}"
echo "bash says: ${VAR}"
printf "\n"

echo "c"
./projects/c/a.out  > "${VAR}"
printf "\n"

echo "c++"
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
node projects/typescript/src/index.js
printf "\n"

echo "zsh"
zsh projects/zsh/hello_world.sh
printf "\n"