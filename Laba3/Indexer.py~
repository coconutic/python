# -*- coding: utf-8 -*-

import os
import json

class Indexer(object):

    def __init__(self):
        self.inverted_index = {}
        self.count_doc = 0

    def check(self, i):
        temp = []
        for j in xrange(3):
            if "\r" in i:
                temp.append(i[:i.index("\r")])
                temp.append(i[i.index("\r") + 1:])
                i = ''.join(temp)
            if "\n" in i:
                i = i[:-1]
            if "\t" in i:
                temp.append(i[:i.index("\t")])
                temp.append(i[i.index("\t") + 1:])
                i = ''.join(temp)
        return i

    def add_doc(self, text):
        self.count_doc += 1
        for i in text:
            i = self.check( i)
            if i in ["", " ", "\n", "\t"]:
                continue
            if i not in self.inverted_index:
                self.inverted_index[i] = []
            self.inverted_index[i].append(self.count_doc)
            
    def store(self, path):
        file_name = os.path.join(path, 'inverted_index')
        f = open(file_name, "w")
        json.dump(self.inverted_index, f, sort_keys=True, indent=4)
        
def start(directory_dir):
    indexer = Indexer()
    for i in os.listdir(directory_dir):
        f = open(os.path.join(directory_dir, i))
        parse_text = f.read().split(" ")
        indexer.add_doc(parse_text)
    indexer.store(directory_dir)

def main():
    start('/home/katrin/database')

if __name__ == "__main__":
    main()
