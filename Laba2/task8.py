#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def cached(func):
    def f(*args, **kwargs):
        key = tuple(kwargs.keys())
        value = tuple(kwargs.values())
        if (args, key, value) in f.storage.keys():
            return f.storage[(args, key, value)]
        else:
            temp = func(*args, **kwargs)
            f.storage[(args, key, value)] = temp
        return temp
    f.storage = {}
    return f

@cached
def sum(a, b):
    s = 0
    while a != b:
        s += a
        a += 1
    return s

