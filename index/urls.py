from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
# from . import settings
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path("", views.index, name="index"),
]