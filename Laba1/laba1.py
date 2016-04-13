#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import argparse
import re


def openfile(a):
    with open(a) as file:
        return file.read()

def div_sentens(a):
    punct = ['.', '?', '!']
    list_of_senten = []
    temp = ""
    
    for i in a:
        if i in punct:
            list_of_senten.append(temp)
            temp = ""
            continue
        temp += i
    return list_of_senten


def div_into_words(a):
    punct = ['.', ',', '!', '?', '(', ')']
    temp = ""
    for i in a:
        if i in punct:
            continue
        temp += i
    list_of_words = temp.split(" ")

    while "" in list_of_words:
        list_of_words.remove("")

    return list_of_words


def div_to_int(a):
    data = div_into_words(a)
    return map(int, data)


def count_words(a):
    list_words = div_into_words(a)  
    d = {}
    
    for word in list_words:
        if d.get(word) == None:
            d[word] = 1
        else:
            d[word] += 1
    return d


def avarage_cn(a):
    count_sentense = len(div_sentens(a))
    count_words = len(div_into_words(a))

    return count_words / count_sentense

def median_count(a):
    list_len = []
    list_of_senten = div_sentens(a)
    list_of_words = []

    for i in list_of_senten:
        list_of_words = div_into_words(i)
        list_len.append(len(list_of_words))
        list_of_words = []

    list_len.sort()
    length = len(list_len)

    if length % 2 == 0:
        return list_len[(length / 2) - 1]
    else:
        return list_len[length / 2]


def n_gramm(a, N, K):
    list_words = div_into_words(a)

    top = {}
    temp = []
    count = 0

    for i in list_words:
        for j in xrange(len(i) - N + 1):
            temp.append(i[j:j + N])

    for word in temp:
        if top.get(word) == None:
            top[word] = 1
        else:
            top[word] += 1
    d = top.items()

    d.sort(lambda x, y: 1 if x[1] < y[1] else -1 if x[1] > y[1] else 0)
    
    return  d[:K]


def qsort(s, l, r):
        #быстрая сортировка
    L = l
    R = r
    temp = 0
    middle = s[l + ((r - l) / 2)]
    while l < r:
        while s[l] < middle and l <= R:
            l += 1
        while s[r] > middle and r >= L:
            r -= 1
        if l <= r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
    if (r - L) >= 1:
        qsort(s, L, r)
    if (R - l) >= 1:
        qsort(s, l, R)
    return s

    length = len(s) - 1
    w = qsort(s, 0, length)
    print w


def mergesort(s):
        #сортировка слияния
    s = map(int, s)

    if len(s) > 1:
        p = len(s) / 2
        a = mergesort(s[:p])
        b = mergesort(s[p:])
        s = merge(a, b)
    return s


def merge(a, b):
    s = []
    count_a, count_b = 0, 0
    while count_a < len(a) and count_b < len(b):
        if a[count_a] < b[count_b]:
            s.append(a[count_a])
            count_a += 1
        else:
            s.append(b[count_b])
            if a[count_a] == b[count_b]:
                count_a += 1
            count_b += 1
    while count_a < len(a):
        s.append(a[count_a])
        count_a += 1
    while count_b < len(b):
        s.append(b[count_b])    
        count_b += 1
    return s


#4 пукт(числа фибоначи) 

def fibgenerator(n):
    k1 = 0
    k2 = 1
    x = 0
    while x < n:
        yield k1
        temp = k1
        k1 = k2
        k2 = temp + k2
        x+=1

        
#поразрядная сортировка
def radix_sort(s):
    maximum = 0
    ten_power = [1]
    for i in xrange(1, 50):
        ten_power.append(ten_power[i - 1] * 10)
    for k in s:
        if num_length(k) > maximum:
            maximum = num_length(k)
    for d in range(1, maximum + 1): 
        r = [0] * len(s)
        num = [0] * 10
        for i in s:
            number = (i % ten_power[d]) / ten_power[d - 1]
            num[number] += 1
        new_arr= []
        for i in range(0,10):
            summ = 0
            for j in range(0,i):
                summ += num[j]
            new_arr.append(summ)
        for i in s:
            number = (i % ten_power[d]) / ten_power[d - 1]
            position = new_arr[number]
            r[position] = i
            new_arr[number] += 1
        s = r
    return s


def num_length(a):
    k = 0
    while a > 0 :
        a /= 10
        k += 1
    return k


def validation_email(str):
    c =re.match('\w+\@\w+\.\w+$', str)
    return c


def validation_db(str):
    c = re.match('\d+\.[\d]+$', str)
    return c

def url_todict(str):
    nd = re.match(r'((?P<scheme>\w+)://|.)?'
                  r'(?P<host>[\w\.\-]+)?'
                  r'(:(?P<port>\d+))?'
                  r'(?P<path>[\/\-\w]+[\.[\w]+]*)?'
                  r'(?P<parametr>[?].*)?', str)
    d = nd.groupdict()
    return d


def select_data(input):
    length = len(input)
    
    list_data = input.split(" ")
    for i in list_data:
        if i == "":
            continue
        new_list.append(i)
    new_list = [i for i in list_dataj i != ""]
    while "" in list_data:
        list_data.remove("")

    k = 0
    arr = []
    temp = ""

    for i in list_data:
        if i[0] == "\"" and i[-1] == "\"":
            arr.append(i)
            continue
        if "\"" in i:
            if k == 1:
                temp += i
                arr.append(temp)
                k = 0
                temp = ""
                continue
            k += 1
            temp += i
            temp += " "
            continue
        elif k == 1:
            temp += i
            temp += " "
            continue
        else:
            arr.append(i)
    return arr


def add(storage, input):
    for i in input:
        storage.add(i)
    return storage


def remove(storage, input):
    for j in input:
        if j in storage:
            storage.remove(j)
            return storage
        else:
            print "No key"


def find(storage, input):
   for j in input:
        if j in storage:
            print j + " "


def list(storage):
    print storage


def save(data, filename):
    temp = open(filename,'w')
    for i in data:
        temp.write(i + " ")
    temp.close()


def load(filename):
    storage = set([])

    with open(filename) as file:
        temp = select_data(file.read())
        for i in temp:
            storage.add(i)
        return storage


def grep(data, storage):
    k = re.compile(data)
    for i in storage:
        match = k.match(i)
        if match:
            print "found " + i


def interractive_storage():
    storage = set([])

    while (True):
        methods = ["add", "remove", "list", "find", "save", "load", "grep"]
        inp = raw_input()

        input = select_data(inp)
        key = input[0]
        del input[0]

        if key == methods[0]:
            storage = add(storage, input)
        if key == methods[1]:
            storage = remove(storage, input)
        if key == methods[2]:
            list(storage)
        if key == methods[3]:
            find(storage, input)
        if key == methods[4]:
            save(storage, "storage")
        if key == methods[5]:
            storage = load("storage")
        if key == methods[6]:
            grep(input[0], storage)
            

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Write a name of the file",
                        type=str)
    parser.add_argument("method", help="Choose a method",
                        type=str)
    args = parser.parse_args()

    if args.filename == "interractive":
        data = "interractive"
    else:
        data = openfile(args.filename)
    func = args.method
    
    if func == "counit_words":
        print count_words(data)
    elif func == "avarage_cn":
        print avarage_cn(data)
    elif func == "median_count":
        print median_count(data)
    elif func == "n_gramm":
        N = int(raw_input("Write N: "))
        K = int(raw_input("Write K: "))
        print n_gramm(data, N, K)
    elif func == "qsort":
        s = div_to_int(data)
        print qsort(s, 0, len(s) - 1)
    elif func == "mergesort":
        s = div_to_int(data)
        print mergesort(s)
    elif func == "radix_sort":
        s = div_to_int(data)
        print radix_sort(s)
    elif func == "run" and data == "interractive":
        interractive_storage()
    else:
        print "There is no method in thise programm"
            
if __name__ == "__main__":
    main()
