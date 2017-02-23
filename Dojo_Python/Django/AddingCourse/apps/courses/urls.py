from django.conf.urls import url, include
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^course$', views.course),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^destroy/delete/(?P<id>\d+)$', views.delete),
    url(r'^comments/(?P<id>\d+)$', views.comments),
    url(r'^comments/addcomment/(?P<id>\d+)$', views.addcomment)
]
