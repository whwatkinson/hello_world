#!/usr/bin/env bash

bend run hello_world.bend > hello.txt

# Conform output to match other projects
sed -n 's/^Result: "\(.*\)"/\1/p' hello.txt
