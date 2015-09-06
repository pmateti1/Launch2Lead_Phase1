from django.conf.urls import url
from authentication import views

urlpatterns = [
    url(r'^$', views.Launch2LeadRegistration, name='register'),
    # url(r'^register/$', views.Launch2LeadRegistration),
    # url(r'^$', views.user_login, name='login'),
    # url(r'^$', views.index, name='index'),
 ]
