import Search_str
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index_url(request):
#    if (request.GET.url('add_url')):
 #       t = "r"
    return render(request, 'search/index_url.html')

def find_res(request):
    s = Search_str.Search(request.GET.get('text'))
    ans=  s.start()
    return HttpResponse(json.dumps({'urls': ans}), content_type="application/json")

def urls(request):
    return render(request, 'search/urls.html')

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

