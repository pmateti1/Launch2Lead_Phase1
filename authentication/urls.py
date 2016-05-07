from django.conf.urls import url
from authentication import views


urlpatterns = [
    url(r'^login/$', views.Authenticate_1, name='login'),
    url(r'^logout/$', views.LogoutRequest, name='logout'),
    url(r'^recover/$', views.reset, name='reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.reset_confirm, name='password_reset_confirm'),
    url(r'^success/$', views.success, name='success'),
 ]
