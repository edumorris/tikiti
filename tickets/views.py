from multiprocessing import context
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Authentication imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def page_not_found_view(request, exception):
    context = {
        "title": "etikiti - 404 Page Not Found",
    }
    return render(request, "404.html", context, status=404)
    
def user_login(request): # Login page
    context = {
        "title": "etikiti - Login"
    }
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.warning(request, "The Username or Password is incorrect")
            return redirect(user_login)
    else:
        return render(request, 'user_management/login.html', context)
    
    
def events_view(request): # Homepage
    context = {
        "title": "etikiti - Events"
    }
    
    return render(request, "events.html", context)