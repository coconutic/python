#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import argparse
from random import *

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-cf", "--countFields", help="Write number of fields.", type=int)
    parser.add_argument("-tf", "--typeFields", help="Write numbers or ASCII", type=str)
    parser.add_argument("-t", "--field_separator", help="Write a separator of fields", type=str)
    parser.add_argument("-ls", "--line_separator", help="Write a sepapator of str", type=str)
    parser.add_argument("-cs", "--countStr", help="Write number of str", type=int)

    args = parser.parse_args()
    
    countFields = 5
    typeFields = "numbers"
    sepFields = '\t'
    sepStr = '\n'
    countStr = 8000000

    if args.countFields:
        countFields = args.countFields
    if args.typeFields:
        typeFields = args.typeFields
    if args.field_separator:
        sepFields = args.field_separator
    if args.line_separator:
        sepStr = args.line_separator
    if args.countStr:
        countStr = args.countStr

    f = open("gen", 'w')

    if typeFields == "numbers":
        for i in xrange(countStr):
            for j in xrange(countFields):
                field = randrange(-1000000, 1000000, 1)
                f.write(str(field))
                if j != countFields - 1:
                    f.write(sepFields)    
            f.write(sepStr)
    else:
        for i in xrange(countStr):
            for j in xrange(countFields):
                for k in xrange(randrange(1, 10)):
                    field = chr(randrange(0, 255))
                    f.write(field)
                if j != countFields - 1:
                    f.write(sepFields)
            f.write(sepStr)

    f.close()

if __name__ == "__main__":
    main()
