from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login as auth_login
from django.http.response import HttpResponseRedirect
from user.forms import UserForm
from django.contrib.auth.models import User

from main.functions import generate_form_errors

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)

                return HttpResponseRedirect("/")

        context = {
            "title" : "Login",
            "error": True,
            "message": "Invalid username or password"
        }    
        return render(request, "users/login.html", context=context)

    else: 

        context = {
            "title": "Login",
        }    
        return render(request, "users/login.html", context=context)

