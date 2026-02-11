#!/usr/bin/env bash

systemctl start redis-server

echo 'SET helloworld "Hello, World!"' | redis-cli > /dev/null

echo 'GET helloworld' | redis-cli > output.txt

tail -n 1 output.txt
