#!/usr/bin/env zsh

echo "c:"
./c/a.out
echo "\n"

echo "cpp:"
./cpp/a.out
echo "\n"

echo "golang:"
./golang/main
echo "\n"


echo "rust:"
./rust/main
echo "\n"

echo "node:"
unset NODE_OPTIONS
node javascript/index.js
echo "\n"

echo "python:"
python3 python/hello_world.py
echo "\n"

echo  "zsh"
./zsh/hello_world.sh
echo "\n"

echo  "bash"
./bash/hello_world.sh
echo "\n"
