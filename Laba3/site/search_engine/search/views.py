from django.shortcuts import render
from django.http import HttpResponse



def search(request):
    return render(request, 'search/search.html')
