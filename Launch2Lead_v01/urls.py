from django.conf.urls import url
from Launch2Lead_v01 import views

urlpatterns = [
    # url(r'^$', views.register, name='register'),
    # url(r'^$', views.user_login, name='login'),
    url(r'^$', views.index, name='index'),
 ]
