#!/usr/bin/env bash

./compile.sh
printf "\n\n\n\n\n\n\n"

echo "*********"
echo "SOUND OFF"
echo "*********"
echo " "


echo "Bash says $(bash projects/bash/hello_world.sh -1)"
echo " "

echo "C says $(./projects/c/a.out -1)"
echo " "

echo "C++ says $(./projects/cpp/a.out -1)"
echo " "

echo "Golang says $(./projects/golang/main -1)"
echo " "

echo "JavaScript says $(node projects/javascript/index.js -1)"
echo " "

echo "Python says $(python3 projects/python/hello_world.py -1)"
echo " "

echo "Rust says $(./projects/rust/main -1)"
echo " "

echo "TypeScript says $(node projects/typescript/src/index.js -1)"
echo " "

echo "Zsh says $(zsh projects/zsh/hello_world.sh -1)"
echo " "
