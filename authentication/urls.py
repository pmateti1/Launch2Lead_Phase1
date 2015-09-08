from django.conf.urls import url
from authentication import views

urlpatterns = [
    url(r'^$', views.Authenticate_1, name='register'),
    url(r'^logout/$', views.LogoutRequest, name='logout'),
    url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),

    # url(r'^register/$', views.Launch2LeadRegistration),
    # url(r'^$', views.user_login, name='login'),
    # url(r'^$', views.index, name='index'),
 ]
