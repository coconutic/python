#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def checkInput1(func):
    def input(a):
        if isinstance(a, (int, long)):
            return func(a)
        return False
    return input


def checkInput2(func):
    def input(a, b):
        if isinstance(a, (int, long)) and isinstance(b, (int, long)):
            return func(a, b)
        return False
    return input


def checkInput3(func):
    def input(a, b, h):
        if isinstance(a, (int, long)) and isinstance(b, (int, long)) and \
        (h, (int, long)):
            return func(a, b, h)
        return False
    return input


@checkInput1
def myxrange1(index):
    print "he"
    i = 0
    while i < index:
        yield i
        i += 1


@checkInput2
def myxrange2(start, end):
    i = start
    while i < end:
        yield i
        i += 1


@checkInput3
def myxrange3(start, end, h):
    i = start
    while i < end:
        yield i
        i += h

class myxrange(object):
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0
            self.h = 1
            self.length = args[0]
        if len(args) == 2:
            self.start = args[0]
            self.h = 1
            self.length = args[1]
        if len(args) == 3:
            self.start = args[0]
            self.h = args[2]
            self.length = args[1]

    def __iter__(self):
        while self.start < self.length:
            yield self.start
            self.start += self.h
        raise StopIteration

    def __reversed__(self):
        while self.length != self.start:
            yield self.length
            self.length -= self.h

    def __getitem__(self, key):
        ans = self.start + key * self.h
        return ans








