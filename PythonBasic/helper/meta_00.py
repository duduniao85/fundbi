#!/usr/bin/env python
# coding: utf-8
#http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Metaprogramming.html
#元编程技巧 使用元类进行面对对象编程

def howdy(self, you):
    print("Howdy, " + you)

MyList = type('MyList', (list,), dict(x=42, howdy=howdy))

ml = MyList()
ml.append("Camembert")
print(ml)
print(ml.x)
ml.howdy("John")