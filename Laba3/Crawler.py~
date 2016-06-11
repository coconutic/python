# -*- coding: utf-8 -i*-

import sys
import requests
import urlparse
import os.path
import base64

from threading import Thread
from Queue import Queue
from bs4 import BeautifulSoup

class Crawler(object):

    def __init__(self, depth, count, cur_url, storage_dir):
        self.url = cur_url
        self.q = Queue()
        self.depth = depth
        self.listOfThreads = []
        self.q.put((self.url, 0))
        self.path = storage_dir

        for i in xrange(count):
            t = Thread(self.todo())
            t.signal = True
            t.daemon = True
            self.listOfThreads.append(t)

    def write_into_file(self, u, txt):
        file_name = os.path.join(self.path, base64.b16encode(u))
        f = open(file_name, "w")
        soup = BeautifulSoup(txt, 'html.parser')
        data = soup.get_text()
        for i in data:
            try:
                f.write(i.encode("utf-8")) 
            except Exception:
                print i
                print "_------------------------------"
        f.close()
        sys.stdout.flush()
        return

    def todo(self):
        while True:
            try:
                self.do()
            except Exception:
                pass

    def downloadPages(self):
        for i in self.listOfThreads:
            i.start()
            
    def absolut_url(self, u):
        temp = urlparse.urljoin(self.url, u)
        if '#' in temp:
            temp = temp[:temp.index('#')]
        return temp

    def download(self, u):
        page = requests.get(u) #downland page of site 
        if  page.status_code != 200:
            raise Exception(page.status_code)
        return page.text
    
    def findURLs(self, u):
        page = self.download(u)
        self.write_into_file(u, page)
        print "hea!!!!"
        soup = BeautifulSoup(page, 'html.parser') #beautiful  HTML
        listOfUrls = []
        for url in soup.find_all('a'):
            listOfUrls.append(self.absolut_url(url.get('href')))
        return listOfUrls
            
    def do(self):
        temp = self.q.get()
        link = temp[0]
        depth = temp[1]
        print link
        if depth > self.depth:
            print "CurDepth > inputDepth"
            return
        listOfURLs = self.findURLs(link)
        for i in listOfURLs:
            self.q.put((i, depth + 1))
        

def main():
    a = Crawler(3, 5, 'http://docs.python.org/', '/home/katrin/database/')
    k = a.downloadPages()

if __name__ == "__main__":
    main()
