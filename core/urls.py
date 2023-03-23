from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('user-add-page/', adduser, name='adduser')
]
