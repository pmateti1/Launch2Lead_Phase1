from django.conf.urls import url
from authentication import views


urlpatterns = [
    url(r'^$', views.Authenticate_1, name='register'),
    url(r'^logout/$', views.LogoutRequest, name='logout'),
    url(r'^recover/$', views.reset, name='reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.reset_confirm, name='password_reset_confirm'),
    url(r'^success/$', views.success, name='success'),
    # url(r'^$', views.user_login, name='login'),
    # url(r'^$', views.index, name='index'),
 ]
