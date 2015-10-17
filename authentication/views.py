from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from authentication.forms import RegistrationForm, LoginForm


@csrf_protect
def Authenticate_1(request):
    if request.method == 'POST':
        if "confirmsignin" in request.POST:
            form_auth = LoginForm(request.POST)
            if form_auth.is_valid():
                # username = form_auth.cleaned_data['username']
                # password = form_auth.cleaned_data['password']
                user = authenticate(email=request.POST['email'], password=request.POST['password'])
                print ("this is 1")
                # launchers = auth.authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                    return redirect('/')
            else:
                form_auth = LoginForm()
                print ("this is error1")
            return render_to_response('Launch2Lead/password_reset/login.html', {'form_auth': form_auth},
                                          context_instance=RequestContext(request))
        if "confirmsignup" in request.POST:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(username=form.cleaned_data['username'],
                                                email=form.cleaned_data['email'],
                                                password=form.cleaned_data['password'])
                user.save()
                print ("this is 2")
                return redirect("/")
                # launchers = UserProfile.objects.get_or_create(user=user, email=form.cleaned_data['email'])[0]
                # launchers.save()
                # return render_to_response('Launch2Lead/password_reset/login.html', {'form': form},
                #                       context_instance=RequestContext(request))
            else:
                form = RegistrationForm()
                print ("this is error2")
            return render_to_response('Launch2Lead/password_reset/login.html', {'form', form},
                                      context_instance=RequestContext(request))
        else:
            print ("this is error3")
            form = RegistrationForm()
            form_auth = LoginForm()
        return render_to_response('Launch2Lead/password_reset/login.html', {'form': form, 'form_auth': form_auth},
                                  context_instance=RequestContext(request))
    else:
        print ("this is error4")
        form = RegistrationForm()
        form_auth = LoginForm()
    return render_to_response('Launch2Lead/password_reset/login.html', {'form': form, 'form_auth': form_auth},
                              context_instance=RequestContext(request))




def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')

def reset(request):

    return password_reset(request, template_name='Launch2Lead/password_reset/reset.html',
        email_template_name='Launch2Lead/password_reset/reset_email.html',
        subject_template_name='Launch2Lead/password_reset/reset_subject.txt',
        post_reset_redirect=reverse('success'))

def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='Launch2Lead/password_reset/reset_confirm.html',
        uidb36=uidb36, token=token, post_reset_redirect=reverse('success'))

def success(request):
  return render_to_response(request, "Launch2Lead/password_reset/success.html")