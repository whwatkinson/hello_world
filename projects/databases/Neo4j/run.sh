#!/usr/bin/env bash

cat output.txt | tail -1 | sed "s/\"//g"
