# -*- coding: utf-8 -*-

from collections import OrderedDict
import os
import base64
import json

class Indexer(object):

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

        for k, v in text.iteritems():
            print k
            try:
                word = db.objects.get(name=str(k))
            except:
                in_w = db(name=str(k))
                in_w.save()
            finally:
                word = db.objects.get(name=str(k))
                word.count_in_file_set.create(countWord=, link_id=self.count_doc)
                self.count_doc += 1
                word.save()

            
def start(directory_dir):
    indexer = Indexer()
    for i in os.listdir(directory_dir):
        f = open(os.path.join(directory_dir, i))
        parse_text = f.read()
        parse_text = indexer.check(parse_text)
        indexer.add_doc(parse_text.split(" "), i)
    indexer.store()

def main():
    start('/home/katrin/database')

if __name__ == "__main__":
    import sys
    import django
    sys.path.append('/home/katrin/python/Laba3/site/search_engine/')
    os.environ['DJANGO_SETTINGS_MODULE']='search_engine.settings'
    django.setup()

    from search.models import Indexer as db

    main()
