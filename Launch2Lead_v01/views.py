from django.shortcuts import render_to_response
from django.template.context import RequestContext
# from django.contrib.auth import authenticate, login
# from django.http import HttpResponseRedirect, HttpResponse
#
# from authentication.forms import UserForm



# Create your views here.
def index(request):
    return render_to_response("Launch2Lead/index.html", context_instance=RequestContext(request))

def KnowledgeDocuments(request):
    return render_to_response("Launch2Lead/knowledge_doc.html", context_instance=RequestContext(request))

def story_animation_slider(request):
    return render_to_response("Launch2Lead/Launch2Lead_story.html", context_instance=RequestContext(request))
