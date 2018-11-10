#!/usr/bin/python
try:
    val  = 10/0
except ZeorDivisionError as ex:
    print(ex)
