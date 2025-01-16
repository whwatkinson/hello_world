#!/usr/bin/env bash

echo -n "Bash: " && bash main.c
gcc main.c -o main.c.out && echo -n "C: " && ./main.c.out
g++ main.c -o main.cpp.out && echo -n "C++: " && ./main.cpp.out
echo -n "CoffeeScript: " && coffee main.c
#echo -n "Fish: " && fish main.c
echo -n "Julia: " && julia main.c
echo -n "Perl: " && perl main.c && echo ""
#echo -n "PHP: " && php main.c
echo -n "Python 2: " && python2 main.c
echo -n "Python 3: " && python3 main.c
echo -n "Ruby: " && ruby main.c && echo ""
rustc main.c -o main.rust && echo -n "Rust: " && ./main
echo -n "Nim: " && ./main
echo -n "Sh: " && sh main.c
#echo -n "Tsh: " && tsh main.c
echo -n "Zsh: " && sh main.c