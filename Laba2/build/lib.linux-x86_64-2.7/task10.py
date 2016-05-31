# -*- coding: utf-8 i-*i_

class Iter(object):

    def __init__(self, s):
        self.data = s

    def __iter__(self):
        return self.data.__iter__()

    def filter(self, f):
        ans = Iter((x for x in self.data if f(x)))
        return ans
        

def f(x):
    return x < 20

def f2(x):
    return x > 10

def i(x):
    x = 0
    while True:
        yield x
        x += 1

def main():
    #a = Iter((i for i in xrange(123))) 
    a = Iter([1, 2, 3, 4, 100, 123, 13, 32])
    first = []
    for i in a:
        first.append(i)
        if i == 100:
            break
    second = []
    for i in a:
        second.append(i)
    print "Before 432 = {}".format(first)
    print "All elements = {}".format(second)
    for i in  a.filter(f).filter(f2):
        print i
    for i in a:
        print i

if __name__ == "__main__":
    main()
