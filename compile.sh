#!/usr/bin/env bash

echo "*********"
echo "COMPILING"
echo "*********"
echo " "

echo "Compiling c"
cd projects/c/ || exit
cc main.c

echo "Compiling c++"
cd ../cpp/ || exit
cc main.cpp

echo "Compiling golang"
cd ../golang/ || exit
go build main.go

echo "Compiling rust"
cd ../rust/ || exit
rustc main.rs

echo "Compiling typescript"
cd ../typescript/src || exit
tsc index.ts
