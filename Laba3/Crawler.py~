# -*- coding: utf-8 -*-

import requests
import urlparse
from threading import Thread
from Queue import Queue
from bs4 import BeautifulSoup

class Crawler(object):

    def __init__(self, depth, count, cur_url):
        self.url = cur_url
        self.q = Queue()
        self.depth = depth
        self.listOfThreads = []
        self.q.put((self.url, 0))

        for i in xrange(count):
            t = Thread(self.todo())
            self.listOfThreads.append(t)

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
        soup = BeautifulSoup(self.download(u), 'html.parser') #beautiful  HTML
        listOfUrls = []
        for url in soup.find_all('a'):
            listOfUrls.append(self.absolut_url(url.get('href')))
        return listOfUrls
            
    def do(self):
        temp = self.q.get()
        link = temp[0]
        depth = temp[1]
        print link
        print depth
        if depth > self.depth:
            print "CurDepth > inputDepth"
            return
        listOfURLs = self.findURLs(link)
        for i in listOfURLs:
            self.q.put((i, depth + 1))
        

def main():
    a = Crawler(2, 50, 'http://stackoverflow.com/questions/4019971/how-to-implement-iter-self-for-a-container-object-python')
    k = a.downloadPages()

if __name__ == "__main__":
    main()
