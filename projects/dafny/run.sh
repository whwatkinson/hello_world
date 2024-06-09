#!/usr/bin/env bash

dafny /compile:3 hello_world.dfy | tail -1
