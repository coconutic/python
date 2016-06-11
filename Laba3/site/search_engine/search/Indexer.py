# -*- coding: utf-8 -*-

from collections import OrderedDict
from django.db import transaction
import os
import sys
import django
sys.path.append('/home/katrin/python/Laba3/site/search_engine/')
os.environ['DJANGO_SETTINGS_MODULE']='search_engine.settings'
django.setup()

from search.models import Indexer
from search.models import Count_in_file
import base64
import json

class Inde(object):

    def __init__(self):
        self.count_doc = 0

    def check(self, i):
        array = [ ',', "\n", "\r", "\"", "\t", '#', ')', '(', '$', '!', '&', '?', ':', ';', '^']

        without = []
        for c in i:
            if c in array:
                without.append(' ')
            else:
                without.append(c)

        return ''.join(without)
    
    @transaction.atomic
    def add_group_index(self, listwords):
        for word in listwords:
            index = Indexer(name=word)
            index.save()

    @transaction.atomic
    def add_group_files(self, listfiles):
        for f in listfiles:
            index = Count_in_file(countWords=f[1], link=f[0])
            index.indexer = f[2]
            index.save()


    def add_doc(self, text, filename):
        print str(base64.b16decode(filename))
        self.count_doc += 1

        splitted_text = []

        for i in text:
            if i != '':
                splitted_text.append(i)

        text = {}

        for i in splitted_text:
            if i in text:
                text[i] += 1
            else:
                text[i] = 1

        temp = []
        for word in text.keys():
            query_result = list(Indexer.objects.raw('SELECT * FROM search_indexer WHERE name=%s', [word]))
            if len(query_result) == 0:
                temp.append(word)
        self.add_group_index(temp)
        
        lw = []
        for k, v in text.iteritems():
            query_result = list(Indexer.objects.raw('SELECT * FROM search_indexer WHERE name=%s', [k]))
            lw.append((filename, v, query_result[0]))
        self.add_group_files(lw)

def start(directory_dir):
    indexer = Inde()
    for i in os.listdir(directory_dir):
        f = open(os.path.join(directory_dir, i))
        parse_text = f.read()
        parse_text = indexer.check(parse_text)
        indexer.add_doc(parse_text.split(" "), i)

def main():
    start('/home/katrin/database')

if __name__ == "__main__":
    main()
