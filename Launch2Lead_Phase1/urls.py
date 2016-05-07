"""Launch2Lead_Phase1 URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from Launch2Lead_v01 import views


urlpatterns = [
    url(r'^', include('authentication.urls')),
    url(r'^', include('knowledge_documents.urls')),
    url(r'^', include('Launch2Lead_v01.urls')),
    url(r'^', include('circle.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^Launch2Lead_story', views.story_animation_slider, name='storyanimi'),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
]
