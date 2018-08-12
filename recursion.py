#!/usr/bin/python
def fib(n):
    if n==1 or n==2:
        return n
    else:
        return fib(n-1) + fib(n-2)

while 1:
    
    print("enter which fibonacci term you want")
    n = int(input())
    print(fib(n))
