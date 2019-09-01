"""order URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# coding=utf-8
from django.conf.urls import include, url,patterns
from django.contrib import admin
import os,settings
# import
urlpatterns = [
    url(r'^admin/',include(admin.site.urls) ),
    url(r'^customer/','dian.views.custumer'),
    url(r'^submite','dian.views.submite'),
    url(r'^log','dian.views.login'),
    url(r'^denglu','dian.views.denglu'),
    url(r'^show','dian.views.xianshi'),
    url(r'^css/(?P<path>.*)$', 'static.serve',
        {'document_root':settings.STATIC_ROOT+'css/'}),
    url(r'^js/(?P<path>.*)$', 'static.serve',
        {'document_root':settings.STATIC_ROOT+'js/'}),
    url(r'^image/(?P<path>.*)$', 'static.serve',
        {'document_root':settings.STATIC_ROOT+'images/'}),

]


