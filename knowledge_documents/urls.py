__author__ = 'Pranava'
from django.conf.urls import url
from knowledge_documents import views

urlpatterns = [
    url(r'^knowledge_bucket$', views.view_post, name='knowledgeBlog'),
    url(r'^knowledge_bucket/my_first_blog$', views.view_post_detail, name='knowledgeBlog'),
    url(r'^knowledge_bucket/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
 ]
