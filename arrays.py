#!/usr/bin/python
l = list(())
#l.append(1)
print("enter number of elements in the array")
n = int(input())
for i in range(n):
#    print(i)
    l.append(int(input()))
print("the array elements are ")    
for a in l:
    print(a)

l.reverse()
l.sort()
l.pop(1)
print("after reverse, sort, pop(1) ")
for a in l:
    print(a)
