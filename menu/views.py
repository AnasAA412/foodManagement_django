import json
from django.shortcuts import render , get_object_or_404
from django.http.response import HttpResponseRedirect
from menu.models import Category, MenuItem

# Create your views here.
def menu(request):
   
    categoriess = Category.objects.all()
    menuitems = MenuItem.objects.all()
    

    print(categoriess)
    print(menuitems)

    context = {
        
        "categoriess": categoriess,
        "menuitems": menuitems
    }
    return render(request,"home.html",context)

def order(request):
    menuitems = MenuItem.objects.filter(is_ordered=True)
    context = {
        "menuitems" : menuitems,
    }
    return render(request,"order.html",context=context)   

def is_ordered(request,id):
    

    instance = get_object_or_404(MenuItem,id=id)

    instance.is_ordered = True

    
    instance.save()
    

    return HttpResponseRedirect("/home")




