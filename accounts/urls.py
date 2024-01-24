from django.urls import path
from .views import register, user_login, dashboard,logout_view

urlpatterns = [
    path('register/', register, name='register'),
    path('', user_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]
