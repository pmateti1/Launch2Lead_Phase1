from django.shortcuts import render_to_response
from django.template.context import RequestContext
# from django.contrib.auth import authenticate, login
# from django.http import HttpResponseRedirect, HttpResponse
#
# from authentication.forms import UserForm



# Create your views here.
def index(request):
    return render_to_response("Launch2Lead/index.html", context_instance=RequestContext(request))

#
# def register(request):
#     context = RequestContext(request)
#     registered = False
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         if user_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.set_password(user.password2)
#             if user.password <> user.password2:
#                 return HttpResponse("Your Passwords don't match")
#             else:
#                 user.save()
#             registered = True
#         else:
#             print user_form.errors
#     else:
#         user_form = UserForm()
#     #
#     return render_to_response(
#         'Launch2Lead/index.html',
#         {'user_form': user_form, 'registered': registered},
#         context)
#
#
# def user_login(request):
#     context = RequestContext(request)
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/Launch2Lead_v01/')
#             else:
#                 return HttpResponse("Your Launch2Lead account is disabled.")
#
#         else:
#             print "Invalid login details: {0}, {1}".format(username, password)
#             return HttpResponse("Invalid login details supplied.")
#
#     else:
#         return render_to_response('Launch2Lead/index.html', {'login': login}, context)
