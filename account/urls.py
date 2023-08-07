from django.urls import path
from account.views import *


urlpatterns=[
    path('register/',UserRegisterationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('changepassword/',UserChangePassword.as_view(),name='changepassword'),
    


]