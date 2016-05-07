__author__ = 'Pranava'
from django.conf.urls import url
from knowledge_documents import views

urlpatterns = [
    url(r'^knowledge_bucket$', views.view_post, name='knowledgeBlog'),
    url(r'^knowledge_bucket/Post/(?P<slug>\S+)$', views.PostDetail.as_view(), name="post_detail"),
    url(r'^knowledge_bucket/market/(?P<slug>\S+)$', views.MarketResearchDetail.as_view(), name="market_detail"),
 ]
