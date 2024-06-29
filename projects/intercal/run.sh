#!/usr/bin/env bash

# Conform output to match other projects
echo "" | intercal hello_world.i | sed "s/w/W/"
echo ""
