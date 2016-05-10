#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def metoDec(func):
    def input(cls, s):
        def met(name, bases, attr):
            cls.path = s
            return func(cls, name, bases, attr)
        return met
    return input

class MetaClass(type):
    
    @metoDec
    def __new__(cls, name, bases, attrs):
        newAttr = {}

        f = open(cls.path)
        line = f.readline()

        while line:
            if '\n' in line:
                line = line[:-1]
            line = line.split('=')
            newAttr[line[0]] = line[1]
            line = f.readline()
        f.close()
        return super(MetaClass, cls).__new__(cls, name, bases, newAttr)

class Ex(object):
    __metaclass__ = MetaClass("/home/katrin/labs/labs python/storage")

o = Ex()
print o.b

