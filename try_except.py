#!/usr/bin/python
#val = 10/0
try:
    print("enter a number")
    x = int(input())
    print(x)
except ZeroDivisionError:
    print("do not divide by zero")
except ValueError:
    print("please enter a valid number")
