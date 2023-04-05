(prn "Hello World")


tar xvf arc3.1.tar

cd arc3.1

mkdir arc

echo "myname" > arc/admins

racket -f as.scm

at the arc prompt:

(load "news.arc")

(nsv)

