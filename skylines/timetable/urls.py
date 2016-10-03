from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^main/$', views.main, name='main'),
    url(r'^main/log_in/', views.log_in, name='log_in'),
    url(r'^main/sign_in/', views.sign_in, name='sign_in'),
    url(r'^$', views.shedule, name='shedule'),
]
