from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http.response import HttpResponseRedirect



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
        return render(request, "login.html", context=context)

    else: 

        context = {
            "title": "Login",
        }    
        return render(request, "login.html", context=context)