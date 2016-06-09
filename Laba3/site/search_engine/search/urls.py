from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^search_results/$', views.find_res, name='find_res'),
    url(r'^index_url/$', views.index_url, name='index_url'),
    url(r'^urls/$', views.urls, name='urls'),
    url(r'^change_index/$', views.change_index, name='change_index'),
]
