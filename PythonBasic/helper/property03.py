#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke
#展示类描述符的用法
class Car(object):
    country = u'中国'
    def __init__(self, length, width, height, owner=None):
        self._owner = owner
        self._length = length
        self._width = width
        self._height = height

    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, value):
        self._owner = value
    @owner.deleter
    def owner(self):
        self._owner = None
    
    @property
    def length(self):
        return self._length
    @length.setter
    def length(self, value):
        assert value>0,"length must larger than 0"
        self._length = value

if __name__ == '__main__':
    a = Car(1.2,1.4,1.5,u'黑板客')
    print a.owner
    del a.owner
    print a.owner
    a.length=-1