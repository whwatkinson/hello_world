#!/bin/bash

echo '(prn "Hello, World!")' | racket -f /usr/lib/arc3.2/as.scm | tail -2 | head -1

