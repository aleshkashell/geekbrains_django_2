from django.urls import path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('edit/', authapp.edit, name='edit'),
    path('register/', authapp.register, name='register'),
    path('verify/<email>/<slug:activation_key>/', authapp.verify, name='verify'),
    path('send_invite/<email>', authapp.send_invite, name='send_invite'),
]     
