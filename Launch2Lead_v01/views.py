
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def index(request):
    return render_to_response("Launch2Lead/index.html", context_instance=RequestContext(request))


def story_animation_slider(request):
    return render_to_response("Launch2Lead/Launch2Lead_story.html", context_instance=RequestContext(request))


