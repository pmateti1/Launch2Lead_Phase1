import urlparse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from authentication.forms import RegistrationForm, LoginForm
from authentication.models import UserProfile
from django.contrib.auth import authenticate, login, logout


def Authenticate_1(request,
                   success_url=None,
                   login_form=LoginForm,
                   form_class=RegistrationForm,
                   template_name='index.html',
                   extra_context=None,
                   **kwargs):

    if request.method == 'POST':
        if "confirmsignin" in request.POST:
            form_auth = login_form(data=request.POST)
            if form_auth.is_valid():
                username = form_auth.cleaned_data['username']
                password = form_auth.cleaned_data['password']
                launchers = authenticate(username=username, password=password)
                if launchers is not None:
                    login(request, launchers)
                    return HttpResponseRedirect('/Launch2Lead/')
                else:
                    return render_to_response('Launch2Lead/index.html', {'form_auth': form_auth},
                                              context_instance=RequestContext(request))

        if "confirmsignup" in request.POST:
            form = form_class(data=request.POST)
            if form.is_valid():
                user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'],
                                                password=form.cleaned_data['password'])
                user.save()
                launchers = UserProfile.objects.get_or_create(user=user, email=form.cleaned_data['email'])[0]
                launchers.save()
                return render_to_response('Launch2Lead/index.html', {'form': form},
                                      context_instance=RequestContext(request))
        return render_to_response('Launch2Lead/index.html', {'Login',login_form, 'Register', form_class})
    else:
        form = RegistrationForm()
        form_auth = LoginForm()
    return render_to_response('Launch2Lead/index.html', {'form': form, 'form_auth': form_auth}, context_instance=RequestContext(request))


def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/Launch2Lead/')
