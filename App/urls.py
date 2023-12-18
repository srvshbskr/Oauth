from django.urls import path
from .views import *
urlpatterns = [
    path('',homepage,name='home'),
    path('login/',loginpage,name='login'),
    path('signup/',signuppage,name='signup'),
    path('logout',logoutpage,name='logout'),
]
