#!/bin/bash

./app & > output.txt

tail -1 output.txt

./app | tail -1