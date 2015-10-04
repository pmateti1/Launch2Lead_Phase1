from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views import generic
from knowledge_documents import models
from knowledge_documents.models import Market_Research
from knowledge_documents.models import Published_Post
from knowledge_documents.models import Essential_Format


def view_post(request):
    return render_to_response("Launch2Lead/knowledge_doc.html", {
        'post_Market': Market_Research.objects.all(), 'post_published': Published_Post.objects.all(),
        'post_formats': Essential_Format.objects.all()
    })


class BlogDetail(generic.DetailView):
    model = models.Market_Research
    template_name = "Launch2Lead/Blog_single_page.html"


def view_post_detail(request):
    return render_to_response("Launch2Lead/Blog_single_page.html", context_instance=RequestContext(request))
