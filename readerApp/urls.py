#!/usr/bin/env python
from django.conf.urls import include, url
import views


urlpatterns=[
    url(r'^(?P<article_id>[0-9]+)/$', views.articlePage, name='title'),
    url(r'^.*$',views.landingPage, name ='views'),
    # ex: /polls/5/results/
]

