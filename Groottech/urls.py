from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('post/<str:pk>',views.post,name='post'),
    path('terms_of_use',views.usage,name='usage'),
    path('PrivacyNotice',views.privacy,name='privacy'),
    path('Contact Us',views.contact,name='contact'),
    
    


    
]
