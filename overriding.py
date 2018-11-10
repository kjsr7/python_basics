#!/usr/bin/python
class A:
    def display(self):
        print("this is class A")
class B(A):
    def display(self):
        print("this is class B")

x = A()
x.display()
y = B()
y.display()
