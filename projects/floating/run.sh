#!/usr/bin/env sh

# Conform output to match other projects
cat output.txt | tail | sed "s/w/W/"
echo ""
