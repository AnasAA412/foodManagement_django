from django.urls import path,include
from menu.views import menu

app_name = "menu"

urlpatterns = [
    path("", menu, name="menu"),
    
]