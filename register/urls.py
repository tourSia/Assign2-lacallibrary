from django.urls import path
from . import views
#from .views import ResetPasswordView
#from django.contrib.auth import views as auth_view


urlpatterns = [
    path('register/', views.register, name='register'),
    #path('change_password/', ResetPasswordView.as_view(name='changer_password')),
   #path('change_password/', views.changer_password, name='changer_password'),
]
