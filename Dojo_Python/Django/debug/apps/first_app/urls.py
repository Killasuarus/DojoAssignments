from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^show/(?P<name>.*$)', views.show),
    url(r'^', views.index),
]
