import sys
import os
import django
import Search_str
import Crawler
import Indexer
import json
import base64
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

sys.path.append('/home/katrin/python/Laba3/site/search_engine/')
os.environ['DJANGO_SETTINGS_MODULE']='search_engine.settings'
django.setup()

from search.models import Indexer
from search.models import Count_in_file

def to_url(request):
    s = request.GET.get('text')
    s = s.split(" ")
    r = []
    for i in s:
        if i != " " and i !="":
            r.append(i)
    a= Crawler.Crawler(0, 1, r, '/home/katrin/databasetemp/')
    try:
        a.downloadPages()
    except Exception, e:
        pass
    try:
        Indexer.start('/home/katrin/databasetemp/')
    except Exception, e:
        print e
    return HttpResponse('Done it')

def index_url(request):
    return render(request, 'search/index_url.html')

def find_res(request):
    s = Search_str.Search(request.GET.get('text'))
    ans= s.start()
    return HttpResponse(json.dumps({'urls': ans}), content_type="application/json")

def urls(request):
    return render(request, 'search/urls.html')

def get_urls():
    r = Count_in_file.objects.all()
    set_urls = set([])
    for i in r:
        set_urls.add(base64.b16decode(i.link))  
    return HttpResponse(json.dumps({'urls': list(set_urls)}), content_type="application/json")

def w_urls(request):
    request_type = request.GET.get('request')
    print request_type

    if request_type == 'get_urls':
        return get_urls()
    elif request_type == 'delete_urls':
        print request.GET.get('urls_to_delete') 
        delete_urls(request.GET.get('urls_to_delete'))
        return HttpResponse('OK')
    return HttpResponse('Wrong request ;(')

def delete_urls(s):
    s = s.split(",")
    for i in s:
        Count_in_file.objects.filter(link=base64.b16encode(i)).delete()


def change_index(request):
    return render(request, 'search/change_index.html')

def search(request):
    t = []
    if (request.GET.get('search')):
        temp = request.GET.get('str')
        for i in xrange(3):
            t.append(temp)
    context = {'user': t}
    return render(request, 'search/search.html', context)
