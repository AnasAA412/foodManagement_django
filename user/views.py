from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http.response import HttpResponseRedirect
from user.forms import UserForm
from django.contrib.auth.models import User

from foodMngnt.main import generate_form_errors

def menu(request): 
    context = {
        "title": "home"
    }
    return render(request, 'home.html',context=context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        if username and password:
            user = authenticate(request, username=username, password=password)
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            
            if user is not None:
                auth_login(request, user)

                return HttpResponseRedirect("/home")

        else:
            print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")

        context = {
            "title" : "Login",
            "error": True,
            "message": "Invalid username or password"
        } 
        # print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")   
        return render(request, "user/login.html", context=context)

    else: 
        print("cccccccccccccccccccccc")
        context = {
            "title": "Login",
        }    
        return render(request, "user/login.html", context=context)

def logout(request):
    auth_logout(request)   
    return HttpResponseRedirect(reverse("web:index"))


def signup(request):
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            instance = forms.save(commit=False)

            user = User.objects.create_user(
                username=instance.username,
                password=instance.password,
                email=instance.email,
                first_name=instance.first_name,
                last_name=instance.last_name
            )

            

            user = authenticate(request, username=instance.username, password=instance.password)
            auth_login(request,user)

            return HttpResponseRedirect("/home")

        else:
            message = generate_form_errors(forms)


            form = UserForm()
            context={
            
            "title": "Signup ",
            "error": True,  
            "message": message,
            "form": form

            }    
            return render(request, "user/signup.html",context=context)

    else:
        form = UserForm()
        context={
            "title": "Signup", 
            "form": form
        }
        return render(request, "user/signup.html", context=context)