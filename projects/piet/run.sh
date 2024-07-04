#!/usr/bin/env bash

# Conform output to match other projects
echo "" | piet hello_world.png | sed "s/w/W/"
echo ""
