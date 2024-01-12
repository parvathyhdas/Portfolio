from django.urls import path
from PersonalApp import views

urlpatterns = [path('',views.indexPage,name="indexPage"),
               path('saveContact/',views.saveContact,name="saveContact"),]