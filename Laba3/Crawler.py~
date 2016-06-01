import requests
from bs4 import BeautifulSoup

class Crawler(object):
    
    def download(self, url):
        page = requests.get(url) #downland page of site 
        if  page.status_code != 200:
            raise Exception(page.status_code)
        return page.text

    def findURLs(self, u):
        soup = BeautifulSoup(self.download(u))
        listOfUrls = []
        for url in soup.find_all('a'):
            listOfUrls.append(url.get('href'))
        return listOfUrls

def main():
    a = Crawler()
    k = a.findURLs('http://stackoverflow.com/questions/4019971/how-to-implement-iter-self-for-a-container-object-python')
    for i in k:
        print i

if __name__ == "__main__":
    main()
