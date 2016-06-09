import os
import base64
import json
from collections import OrderedDict

class Search(object):
    
    def __init__(self, s):
        self.request = s
        self.data = db.objects.all()
        print '____________'
        print db.objects.get(name='any')
        print '_______________'
        f = open('/home/katrin/python/Laba3/inverted_index')
        self.inverted_index = json.loads(f.read())

    def clever_merge(self, a):
        temp = []
        for i in a:
            for j in i.items():
                temp.append(j)
        d = {}
        for i in temp:
            if i[0] in d:
                d[i[0]] += i[1]
            else:
                d[i[0]] = i[1]
        return  OrderedDict(reversed(sorted(d.items(), key=lambda x: x[1])))

    def start(self):
        ans = []
        temp = []
        self.request = self.request.split(" ")
        for word in self.request:
            try:
                temp.append(self.inverted_index[word])
            except Exception:
                continue
        d = self.clever_merge(temp)
        list_files = os.listdir('/home/katrin/database')
        for i in d.keys():
            u = list_files[int(i) - 1]
            ans.append(base64.b16decode(u))
        return ans


def main():
    w = Search('how to sort dict')

if __name__ == "__main__":
    import sys
    import django
    sys.path.append('/home/katrin/python/Laba3/site/search_engine/')
    os.environ['DJANGO_SETTINGS_MODULE']='search_engine.settings'
    django.setup()

    from search.models import Indexer as db
    main()
