from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('staticText',views.staticText,name='staticText'),
    path('dynamicText',views.dynamicText,name='dynamicText'),
    path('beautifulHTML',views.beautifulHTML,name='beautifulHTML'),
    path('attachmentEmail',views.attachmentEmail,name='attachmentEmail'),
]