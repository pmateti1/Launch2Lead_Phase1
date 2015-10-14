from django.shortcuts import render_to_response
from django.views.generic import ListView
from knowledge_documents import models
from knowledge_documents.models import Market_Research
from knowledge_documents.models import Published_Post
from knowledge_documents.models import Essential_Format


def view_post(request):
    Market_Research.objects = Market_Research.objects.all()
    Published_Post.objects = Published_Post.objects.all()
    Essential_Format.objects = Essential_Format.objects.all()
    return render_to_response("Launch2Lead/knowledge_doc.html", {
        'post_Market': Market_Research.objects.all()[:6], 'post_published': Published_Post.objects.all()[:6],
        'post_formats': Essential_Format.objects.all()[:6]
    })


class MarketResearchDetail(ListView):
    model = Market_Research
    template_name = "Launch2Lead/MarketResearch_Detail.html"

    def get_queryset(self):
        slug = self.kwargs['slug']
        title = Market_Research.objects.get(slug=slug)
        return Market_Research.objects.filter(title=title)


class PostDetail(ListView):
    model = models.Published_Post
    template_name = "Launch2Lead/Post_Detail.html"



