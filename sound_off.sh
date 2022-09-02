#!/usr/bin/env sh


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
