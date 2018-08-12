#!/usr/bin/python
class a:
    def __init__(self,age, weight):
        self.age  = age
        self.weight = weight
    def display(noneed):
        print("age is",noneed.age)
        print("weight is",noneed.weight)
        print("the extra var", noneed.x)
    x  = 2
x = a(2,3)
x.display()
#deleting the object property
del x

