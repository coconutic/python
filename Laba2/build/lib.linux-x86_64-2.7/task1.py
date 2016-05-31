#-*- coding: utf-8 -*-

from tempfile import *
import argparse
import sys

class sort(object):

    def __init__(self, field_sep, line_sep, key, numeric, reverse, buf_size, input_file, output_file):
        self.sepFields = field_sep
        self.sepLines = line_sep
        self.keys = key
        self.reverse = reverse
        self.buf_size = buf_size
        self.inputFile = input_file
        self.numeric = numeric
        self.output_file = output_file

    def write_into_file(self, temp, lines):
        for i in lines:
            temp.write(i)
        temp.seek(0)        
 
    def div_into_files(self):
        f = open(self.inputFile)
        tfiles = []
        lbuf = []
        cur_size = 0
        while True:
            line = f.readline()
            if line == "":
                break
            lbuf.append(line)
            cur_size += sys.getsizeof(line)
            if self.buf_size < cur_size:
                temp = TemporaryFile()
                lbuf = self.mergesort(lbuf)
                self.write_into_file(temp, lbuf)
                tfiles.append(temp)
                lbuf = []
                cur_size = 0
        if len(lbuf) != 0:
            temp =  TemporaryFile()
            lbuf = self.mergesort(lbuf)
            self.write_into_file(temp, lbuf)
            tfiles.append(temp)
            lbuf = []
        return tfiles


    def compare_lines(self, line1, line2):
        line1 = line1.split(self.sepFields)
        line2 = line2.split(self.sepFields) 
        if self.numeric:
            line1 = map(int, line1)
            line2 = map(int, line2)
        for i in self.keys:
            if line1[i] == line2[i]:
                continue
            if line1[i] < line2[i]:
                if self.reverse:
                    return False
                return True
            else:
                if self.reverse:
                    return True
                return False


    def check(self):
        f = open(self.output_file)
        while True:
            line1 = f.readline()
            line2 = f.readline()
            if line1 == "" or line2 == "":
                return True
            if self.reverse == False:
                if self.compare_lines(line1, line2):
                    continue
                else:
                    return False
            else:
                if self.compare_lines(line1, line2) == False:
                    continue
                else:
                    return False
        

    def mergesort(self, s):
        if len(s) > 1:
            p = len(s) / 2
            a = self.mergesort(s[:p])
            b = self.mergesort(s[p:])
            s = self.merge(a, b)
        return s



    def merge(self, a, b):
        sortedlist = []
        count_a, count_b = 0, 0
        while count_a < len(a) and count_b < len(b):
            if self.compare_lines(a[count_a], b[count_b]):
                sortedlist.append(a[count_a])
                count_a += 1
            else:
                sortedlist.append(b[count_b])
                count_b += 1
        if count_a < len(a):
            for i in xrange(count_a, len(a)):
                sortedlist.append(a[i])
        if count_b < len(b):
            for i in xrange(count_b, len(b)):
                sortedlist.append(b[i])
        return sortedlist


    def mergefile(self, file1, file2):
        line1 = file1.readline()
        line2 = file2.readline()
        newbuf = []
        flag1 = False
        flag2 = False

        while True:
            if line1 == "":
                flag1 = True
                break
            if line2 == "":
                flag2 = True
                break
            if self.compare_lines(line1, line2):
                newbuf.append(line1)
                line1 = file1.readline()
            else:
                newbuf.append(line2)
                line2 = file2.readline()
        if not flag1:
            while True:
                if line1 == "":
                    break
                newbuf.append(line1)
                line1 = file1.readline() 
        if not flag2:
            index = 0
            while True:
                if line2 == "":
                    break
                newbuf.append(line2)
                line2 = file2.readline()
        print len(newbuf)
        tempfile = TemporaryFile()
        self.write_into_file(tempfile, newbuf)
        return tempfile


    def sort(self):
        tfiles = self.div_into_files()
        temp_files = []
        while True:
            if len(tfiles) == 1:
                break
            if len(tfiles) % 2 == 1:
                temp_files.append(tfiles[len(tfiles) - 1])
                del tfiles[len(tfiles) - 1]
            for i in xrange(0, len(tfiles), 2):
                temp_files.append(self.mergefile(tfiles[i], tfiles[i + 1]))
            tfiles = temp_files[:]
            del temp_files[:]
 
        return tfiles[0]


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-ls","--line_separator", help = "Write the separator between lines", type = str)
    parser.add_argument("-fs","--field_separator", help = "Write the separator between fields", type = str)
    parser.add_argument("-k", "--key", help = "Write lines index", type = list)
    parser.add_argument("-n", "--numeric", help = "Write lines as numbers", type = bool)
    parser.add_argument("--reverse", help = "Specify the sort in reverse order", type = bool)
    parser.add_argument("--check", help = "Check input data", type = bool)
    parser.add_argument("--buffer_size", help = "Write buffer size", type = int)
    parser.add_argument("--input", help = "Write name of input file",type = str)
    parser.add_argument("--output", help = "Write name of outputFile",type = str)

    args = parser.parse_args()

    line_sep = "\n"
    field_sep = "\t"
    key = [0]
    numeric = True
    reverse = False
    check = False
    buf_size = 1000000
    input_file = "gen"
    output_file = "data1"

    if args.line_separator:
        line_sep = args.line_separator
    if args.field_separator:
        field_sep = args.field_separator
    if args.key:
        key = args.key
    if args.numeric:
        numeric = True
    if args.reverse:
        reverse = False
    if args.check:
        check = True
    if args.buffer_size:
        buf_size = args.buffer_size
    if args.input:
        input_file = args.input
    if args.output:
        output_file = args.output


    a = sort(field_sep, line_sep, key, numeric, reverse, buf_size, input_file, output_file)
    if check:
        print a.check()
    else:
        t = TemporaryFile()
        t = a.sort()
        f = open(output_file, 'w')

        while True:
            line = t.readline()
            if line == "":
                break
            f.write(line)

if __name__ == "__main__":
    main()
