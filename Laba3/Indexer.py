# -*- coding: utf-8 -*-

import os
import json

class Indexer(object):

    def __init__(self):
        self.inverted_index = {}
        self.count_doc = 0

    def add_doc(self, text):
        self.count_doc += 1
        for i in text:
            if i not in self.inverted_index:
                self.inverted_index[i] = []
            self.inverted_index[i].append(self.count_doc)
            
    def store(self, path):
        file_name = os.path.join(path, 'inverted_index')
        f = open(file_name, "w")
        json.dump(self.inverted_index, f)
        
def start(directory_dir):
    indexer = Indexer()
    for i in os.listdir(directory_dir):
        f = open(i)
        parse_text = f.read().split(" ")
        indexer.add_doc(parse_text)

def main():
    pass 

if __name__ == "__main__":
    main()
