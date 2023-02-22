from django.shortcuts import render
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