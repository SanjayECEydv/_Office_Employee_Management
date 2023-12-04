
from turtle import home
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path("index/", home),
    path("about/", about),
    path("services/", services),
    path("employee/", include('employee.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
