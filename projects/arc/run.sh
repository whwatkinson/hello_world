#!/bin/bash

echo '(prn "Hello, World!")' | racket -f as.scm | tail -2
