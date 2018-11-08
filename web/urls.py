from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/example/', views.add_exp),
    url(r'^add/sense/', views.add_sense),
    url(r'^add/wnexp/', views.add_wnexp),
    url(r'^add/align/', views.add_align),  
]
