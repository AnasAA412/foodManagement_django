from django.urls import path,include
from menu import views

app_name = "menu"

urlpatterns = [
    path("", views.menu, name="menu"),
    path("orders/", views.order, name="order"),
    path("is_ordered/<int:id>", views.is_ordered, name="is_ordered"),
]