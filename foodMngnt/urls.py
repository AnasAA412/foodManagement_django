
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("user.urls",namespace="user")),
    path('', include("web.urls",namespace="web")),
    path("home/",include("menu.urls",namespace="menu")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
