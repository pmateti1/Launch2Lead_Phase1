from django.conf.urls import url
from circle import views

urlpatterns = [
    url(r'^the_circle$', views.circle1, name='TheCircle'),
 ]
