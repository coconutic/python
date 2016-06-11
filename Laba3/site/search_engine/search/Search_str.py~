import os
import base64
import json
from collections import OrderedDict

import sys
import django
sys.path.append('/home/katrin/python/Laba3/site/search_engine/')
os.environ['DJANGO_SETTINGS_MODULE']='search_engine.settings'
django.setup()

from search.models import Indexer
from search.models import Count_in_file

class Search(object):
    
    def __init__(self, s):
        s = s.split(" ")
        self.request = []
        for i in s:                 
            try:
                temp = Indexer.objects.get(name=str(i))
                t = temp.count_in_file_set.all()
                for j in t:
                    self.request.append(j)
            except:
                continue

    def clever_merge(self):
        d = {}
        print self.request
        for i in self.request:
            if i.link in d.keys():
                d[i.link] += i.countWords
            else:
                d[i.link] = i.countWords
        return  OrderedDict(reversed(sorted(d.items(), key=lambda x: x[1])))

    def start(self):
        ans = []
        d = self.clever_merge()
        for i in d.keys():
            ans.append(base64.b16decode(i))
        return ans


def main():
    w = Search('to')
    print w.start()

if __name__ == "__main__":
    main()
