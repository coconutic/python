# -*- coding: utf-8 -*-

from collections import OrderedDict
import os
import json

class Indexer(object):

    def __init__(self):
        self.inverted_index = {}
        self.count_doc = 0

    def check(self, i):
        array = [ ',', "\n", "\r", "\"", "\t", '#', ')', '(', '$', '!', '&', '?', ':', ';', '^']
        for element in array:
            if element in i:
                i = i.replace(element, '')
        return i

    def add_doc(self, text):
        self.count_doc += 1
        for i in text:
            i = self.check( i)
            if i in ["", " ", "\n", "\t"]:
                continue
            if i not in self.inverted_index:
                self.inverted_index[i] = {}
            if self.count_doc in self.inverted_index[i].keys():
                t =  self.inverted_index[i][self.count_doc] 
                self.inverted_index[i][self.count_doc] += 1
            else:
                 self.inverted_index[i][self.count_doc] = 1

            
    def store(self, path):
        file_name = os.path.join(path, 'inverted_index')
        f = open(file_name, "w")
        self.sort_words()
        json.dump(self.inverted_index, f, indent=4)


    def sort_words(self):
        for k, v in self.inverted_index.items():
            newval = OrderedDict(reversed(sorted(v.items(), key=lambda x: x[1])))
            self.inverted_index[k] = newval



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
