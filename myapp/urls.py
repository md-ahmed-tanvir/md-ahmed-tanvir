from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='Deshboard'),
    path('home/',views.home,name='Home'),
    path('blog/',views.blog,name='Blog'),
    path('about/',views.about,name='About'),
    path('contract',views.contract,name='Contract'),
    

]
