from django.shortcuts import render_to_response
from django.template.context import RequestContext


# Create your views here.
def index(request):
    return render_to_response("Launch2Lead/index.html", context_instance=RequestContext(request))


