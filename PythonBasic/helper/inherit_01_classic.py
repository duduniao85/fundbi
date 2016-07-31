#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke  
# 经典类多重继承
class A:
    a=1
    b=1

class B(A):
    a=2
    
class C(A):
    a=3
    b=3
    c=3
        
class D(B,C):
    pass    


    
if __name__=="__main__":
    d=D()
    
