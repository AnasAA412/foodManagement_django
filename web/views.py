from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        "title": "start"
    }
    return render(request, 'web/index.html', context=context)