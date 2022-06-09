#!/usr/bin/env zsh

echo "c:"
.projects/c/a.out
echo "\n"

echo "cpp:"
.projects/cpp/a.out
echo "\n"

echo "golang:"
.projects/golang/main
echo "\n"


echo "rust:"
.projects/rust/main
echo "\n"

echo "node:"
unset NODE_OPTIONS
node projects/javascript/index.js
echo "\n"

echo "python:"
python3 projects/hello_world.py
echo "\n"

echo  "zsh"
.projects/zsh/hello_world.sh
echo "\n"

echo  "bash"
.projects/bash/hello_world.sh
echo "\n"
