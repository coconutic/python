#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


class Vector(object):

    def __init__(self, list):
        self.list = list


    def __len__(self):
        return len(self.list)
    

    def __str__(self):
        return str(self.list)


    def __add__(self, vector1):
        svector = []
        for i in xrange(len(self)):
            svector.append(self.list[i] + vector1.list[i])
        return svector


    def __sub__(self, vector1):
        svector = []
        for i in xrange(len(self)):
            svector.append(self.list[i] - vector1.list[i])
        return svector


    def __mul__(self, other):
        if isinstance(other, Vector):
           return  self.mulV(other)
        else:
            if isinstance(other, (float, int, long)):
               return self.mulconst(other)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            for i in xrange(len(self)):
                if self.list[i] != other.list[i]:
                    return False
            return True


    def mulconst(self, const):
		ans = 0
        for i in xrange(len(self)):
            ans += self.list[i] * const
        return ans


    def mulV(self, vector1):
		ans = 0
        for i in xrange(len(self)):
            ans += self.list[i] * vector1.list[i]
        return ans


    def getIndex(self, index):
        index -= 1
        for i in xrange(len(self)):
            if i == index:
                return self.list[i]
        return "No value for the given index"


def main():
    myV = Vector([1, 3, 5])
    myV2 = Vector([1, 3, 5])
    a = 2
    print len(myV)
    print myV
    print myV + myV2
    print myV - myV2
    print myV * myV2
    print myV * 2
    print myV == myV2
    v = Vector([1])  
    print myV ==  v


if __name__ == "__main__":
    main()


