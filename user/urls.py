from django.urls import path,include
from user import views

app_name = "user"

urlpatterns = [
    # path('home/',views.home, name='home'),
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
    path('signup/',views.signup, name="signup"),
    path('home/',views.menu, name="menu")
]