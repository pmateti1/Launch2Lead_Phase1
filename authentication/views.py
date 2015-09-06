from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from authentication.forms import RegistrationForm
from authentication.models import UserProfile

def Launch2LeadRegistration(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect('/profile/')
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
                user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
                user.save()
                launchers = UserProfile.objects.get_or_create(user=user, email = form.cleaned_data['email'])[0]
                launchers.save()
                return HttpResponseRedirect('/profile/')
        else:
                return render_to_response('Launch2Lead/index.html', {'form': form}, context_instance=RequestContext(request))
    else:
        '''user is not submitting the form. show them a blank registration form'''
        form=RegistrationForm()
        context = {'form':form}
        return  render_to_response('Launch2Lead/index.html', context, context_instance=RequestContext(request))