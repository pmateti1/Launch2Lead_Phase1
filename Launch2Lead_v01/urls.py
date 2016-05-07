from django.conf.urls import url
from Launch2Lead_v01 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

 ]
