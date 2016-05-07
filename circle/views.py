from django import forms
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from circle.models import Comment


# def circle1(request):
#     return render_to_response("Launch2Lead/The_Circle.html", context_instance=RequestContext(request))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('picture', 'text', 'posted_by')

def circle1(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.save()
        # request.session["email"] = comment.email
        # request.session["website"] = comment.website
        return redirect(request.path)
    return render_to_response('Launch2Lead/The_Circle.html',
                              {
                                  'form': form,
                              },
                              context_instance=RequestContext(request))