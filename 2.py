#!/usr/bin/python
print("Enter your name:")
x = input()
print("Hello, " + x)
print("Enter two numbers")
x = int(input())
y = int(input())
print(x+y)
print(x/y)
print("floor division ", x//y)
print("comparison ", x==y)
comp = x==y
if comp == True:
    print(comp)

print(x is y)
if not(x is 0):
    print("x is not equal to zero")

